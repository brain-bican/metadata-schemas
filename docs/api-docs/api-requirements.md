# API Requirements

This document outlines some specific requirements for portal APIs that would be necessary
for programmatic communication between BCDC, the specimen portal, and the sequencing portal to provide
a central status dashboard for the consortium. This document is an extension of a general [requirements document](https://github.com/BICCN/BICCN-Infrastructure/blob/api-requirements/archive_communication/api-requirements.md)

## Assumptions
- This document and the examples make a few assumptions about the APIs:
    - APIs communicate via JSON over HTTP
    - APIs follow REST principles

## General Requirements

<table class="tg">
<thead>
  <tr>
    <th class="tg-g7sd">#</th>
    <th class="tg-g7sd">Requirement</th>
    <th class="tg-g7sd">Description</th>
    <th class="tg-g7sd">Priority</th>
    <th class="tg-g7sd">Notes</th>
  </tr>
</thead>
<tbody>
  <tr>
  <tr>
    <td class="tg-lboi">1</td>
    <td class="tg-lboi">Service account authentication</td>
    <td class="tg-lboi">A downstream service can authenticate with an API Key to automate interactions with the API.</td>
    <td class="tg-lboi">Must have</td>
    <td class="tg-lboi"></td>
  </tr>
  <tr>
    <td class="tg-lboi">2</td>
    <td class="tg-lboi">Response schemas include BICAN identifiers</td>
    <td class="tg-lboi">A user should be able to query the API using the API's local resource identifier, and retrieve the resource's BICAN identifier.</td>
    <td class="tg-lboi">Must have</td>
    <td class="tg-lboi">
        Supports use case:
        <ul>
            <li>
                <a href="api-use-cases.md#cohesive-view"> Dashboard - One page view of specimen + library + sequencing artifacts </a>
            </li>
        </ul>
    </td>
  </tr>
    <tr>
    <td class="tg-lboi">3</td>
    <td class="tg-lboi">Resources are searchable by BICAN identifiers</td>
    <td class="tg-lboi">
        A user should be able to search resources by BICAN identifiers. Ideally, BICAN identifiers would be directly resolvable to resource (via a PURL system). The API should support retrieving full metadata for a resource with the BICAN identifier.
    </td>
    <td class="tg-lboi">Should have</td>
    <td class="tg-lboi">
        Supports use case:
        <ul>
            <li>
                <a href="api-use-cases.md#cohesive-view"> Dashboard - One page view of specimen + library + sequencing artifacts </a>
            </li>
        </ul>
    </td>
  </tr>
  <tr>
    <td class="tg-lboi">4</td>
    <td class="tg-lboi">Response schemas include status where applicable</td>
    <td class="tg-lboi">
        A user should be able to query the API and receive status for a resource where applicable.
    </td>
    <td class="tg-lboi">Must have</td>
    <td class="tg-lboi">
        Supports use cases:
        <ul>
            <li>
                <a href="api-use-cases.md#specimen-order-summary"> Dashboard - Specimen order status summary </a>
            </li>
            <li>
                <a href="api-use-cases.md#sequencing-order-summary"> Dashboard - Sequencing order status summary </a>
            </li>
        </ul>
    </td>
  </tr>
  <tr>
    <td class="tg-lboi">5</td>
    <td class="tg-lboi">Programmatic update of controlled vocabulary</td>
    <td class="tg-lboi">
        A service account should be able to update controlled vocabulary terms from a centralized repo.
    </td>
    <td class="tg-lboi">Should have</td>
    <td class="tg-lboi">
        Supports use case: 
        <ul>
            <li>
                <a href="api-use-cases.md#vocabulary-updates"> Controlled Vocabulary updates </a>
            </li>
        </ul>
    </td>
  </tr>
  <tr>
    <td class="tg-lboi">6</td>
    <td class="tg-lboi">Programmatic update of biosample metadata</td>
    <td class="tg-lboi">
        A service account should be able to register biosample metadata with specimen portal to update specimen hierarchy
    </td>
    <td class="tg-lboi">Should have</td>
    <td class="tg-lboi">
        Supports use case: 
        <ul>
            <li>
                <a href="api-use-cases.md#biosample-registration"> Biosample registration </a>
            </li>
        </ul>
    </td>
  </tr>
</tbody>
</table>

## Examples

### BICAN identifiers
---


```json
GET https://example.com/api/donor/donor_1

{
    "id": "donor_1",
    "bican_id": "BICAN:donor_1",
    "age": ">89",
    "specimen": [
        {
            "id": "specimen_1",
            "uri": "https://example.com/api/specimen/specimen_1",
        }
    ]
}
```

```json
GET https://example.com/api/specimen/specimen_1

{
    "id": "specimen_1",
    "bican_id": "BICAN:specimen_1",
    "donor_id": {
        "id": "donor_1",
        "url": "https://example.com/api/donor/donor_1"
    },
    "specimen_type": "brain hemisphere",
    "parent_specimen_id": null,
    "child_specimen_ids": [
        {
            "id": "specimen_2",
            "uri": "https://example.com/api/specimen/specimen_2
        },
    ]
}
```

```json
GET https://example.com/api/specimen/specimen_2

{
    "id": "specimen_2",
    "bican_id": "BICAN:specimen_2",
    "specimen_type": "slab",
    "parent_specimen_id": {
        "id": "specimen_1",
        "uri": "https://example.com/api/specimen/specimen_1"
    },
    "child_specimen_ids": [
        {
            "id": "specimen_3",
            "uri": "https://example.com/api/specimen/specimen_3"
        },
        {
            "id": "specimen_4",
            "uri": "https://example.com/api/specimen/specimen_4"
        }
    ]
}
```

### Searching by BICAN ID:
```json
//Filtering via query string
GET https://example.com/api/specimen?bican_id=BICAN:specimen_2

{
    "id": "specimen_2",
    "bican_id": "BICAN:specimen_2",
    "specimen_type": "slab",
    "parent_specimen_id": {
        "id": "specimen_1",
        "uri": "https://example.com/api/specimen/specimen_1"
    },
    "child_specimen_ids": [
        {
            "id": "specimen_3",
            "uri": "https://example.com/api/specimen/specimen_3"
        },
        {
            "id": "specimen_4",
            "uri": "https://example.com/api/specimen/specimen_4"
        }
    ]
}
```

### Status:
```json
GET https://example.com/api/order/order1

{
    "id": "order_1",
    "bican_id": "BICAN:order_1",
    "status": "APPROVED"
}
```

```json
GET https://example.com/api/orders
[
    {
        "id": "order_1",
        "bican_id": "BICAN:order_1",
        "status": "APPROVED"
    },
    {
        "id": "order_2",
        "bican_id": "BICAN:order_2",
        "status": "REJECTED"
    },
    ...
]
```

### Examples of writing to system

```json
POST https://example.com/api/specimen
{
    "bican_id": "BICAN:specimen_5",
    "parent_specimen_bican_id": "BICAN:specimen_2"
    "metadata": {
        "sample_id": "local_identifier_123",
        "specimen_type": "library",
        "creation_date": "11/18/2022 8:00", // Standard datetime
        ...
    }
}
```

```json
PUT https://example.com/api/controlled_vocabulary/specimen_type
{
    "terms": [
        "library",
        "cell in slice"
    ]
}
```



