# API Use Cases

This document outlines use cases for APIs at BICAN portals. 
Requirements supporting the use cases are documented in a separate [requirements doc](api-requirements.md).


## Read use cases
The following use cases describe scenarios where a downstream system would read from a given system's API.

<table id="specimen-order-summary" class="tg">
<thead>
  <tr>
    <th class="tg-0pky">Use case #</th>
    <th class="tg-0pky">1</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0pky">Name</td>
    <td class="tg-0pky">Dashboard - Specimen order status summary </td>
  </tr>
  <tr>
    <td class="tg-0pky">Actors</td>
    <td class="tg-0pky">
        <ul>
            <li>
              BCDC service account
            </li>
            <li>
              Specimen portal
            </li>
        </ul>
    </td>
  </tr>
  <tr>
    <td class="tg-0pky">Description</td>
    <td class="tg-0pky">
        <ul>
            <li>
                PI wants to view summary of all specimen orders' status for their project.
            </li>
            <li>
                BCDC service account queries specimen portal API periodically, maintaining an event log of orders with minimum metadata like status and requesting project. Dashboard reduces event log and displays specimen orders' status for a given project.
            </li>
        </ul>
    </td>
  </tr>
</tbody>
</table>

<table id="specimen-order" class="tg">
<thead>
  <tr>
    <th class="tg-0lax">Use case #</th>
    <th class="tg-0lax">2</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0lax">Name</td>
    <td class="tg-0lax">Dashboard - Specific specimen order status</td>
  </tr>
  <tr>
    <td class="tg-0lax">Actors</td>
    <td class="tg-0lax">
        <ul>
            <li>
                BCDC service account
            </li>
            <li>
                Specimen portal
            </li>
        </ul>
    </td>
  </tr>
  <tr>
    <td class="tg-0lax">Description</td>
    <td class="tg-0lax">
        <ul>
            <li>
                PI sees a particular order for their lab that doesn't match expected status. An order is expected to have been approved and shipped, but instead appears in 'REJECTED' status. PI wants to see more information about the order to see why the order was not approved.
            </li>
            <li>
                The BCDC service account queries specimen portal API, maintaining an event log of order status. Events include BICAN identifier and/or URI for orders that allow redirection to specimen portal for specific information about order. Dashboard reduces event log, displays specific order and links out to the specimen portal to view details.
            </li>
        </ul>
    </td>
  </tr>
</tbody>
</table>

<table id="sequencing-order-summary" class="tg">
<thead>
  <tr>
    <th class="tg-0lax">Use case #</th>
    <th class="tg-0lax">3</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0lax">Name</td>
    <td class="tg-0lax">Dashboard – Sequencing order status summary </td>
  </tr>
  <tr>
    <td class="tg-0lax">Actors</td>
    <td class="tg-0lax">
        <ul>
            <li>
                BCDC service account
            </li>
            <li>
                Sequencing tracker
            </li>
        </ul>
    </td>
  </tr>
  <tr>
    <td class="tg-0lax">Description</td>
    <td class="tg-0lax">
    <ul>
        <li>
            PI wants to view summary of all sequencing orders' status for their project.
        </li>
        <li>
            BCDC service account queries sequencing tracker API periodically, maintaining an event log of orders with minimum metadata like status and requesting project. Dashboard reduces event log and displays specimen orders' status for a given project.
        </li>
    </ul>
  </tr>
</tbody>
</table>

<table id="sequencing-order" class="tg">
<thead>
  <tr>
    <th class="tg-0lax">Use case #</th>
    <th class="tg-0lax">4</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0lax">Name</td>
    <td class="tg-0lax">Dashboard - Specific sequencing order status</td>
  </tr>
  <tr>
    <td class="tg-0lax">Actors</td>
    <td class="tg-0lax">
        <ul>
            <li>
                BCDC service account
            </li>
            <li>
                Sequencing tracker
            </li>
        </ul>
    </td>
  </tr>
  <tr>
    <td class="tg-0lax">Description</td>
    <td class="tg-0lax">
         <ul>
            <li>
                PI sees a particular order for their lab that doesn't match expected status. They want to see more information about the order to see why the status doesn't match.
            </li>
            <li>
                The BCDC service account queries specimen portal API, maintaining an event log of order status. Events include BICAN identifier and/or URI for orders that allow redirection to sequencing portal for specific information about order. Dashboard reduces event log, displays specific order and links out to the sequencing portal to view details.
            </li>
        </ul>
  </tr>
</tbody>
</table>

<table id="cohesive-view" class="tg">
<thead>
  <tr>
    <th class="tg-0lax">Use case #</th>
    <th class="tg-0lax">5</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0lax">Name</td>
    <td class="tg-0lax">Dashboard - One page view of specimen + library + sequencing artifacts</td>
  </tr>
  <tr>
    <td class="tg-0lax">Actors</td>
    <td class="tg-0lax">
        <ul>
            <li>
              BCDC service account
            </li>
            <li>
              Sequencing tracker
            </li>
            <li>
              Specimen portal
            </li>
        </ul>
    </td>
  </tr>
  <tr>
    <td class="tg-0lax">Description</td>
    <td class="tg-0lax">
         <ul>
            <li>
                PI needs to find donor information for a specific sequenced cell from a specific order.
            </li>
            <li>
                The BCDC service account queries specimen portal and sequencing portal API, maintaining an event log of order metadata. Order metadata includes identifiers and URIs for specimen. Specimen resources are queried to retrieve donor ID, and user is redirected to donor page.
            </li>
        </ul>
  </tr>
</tbody>
</table>


## Write use cases
The following use cases describe scenarios where a downstream system/person needs to write information back to a given portal's system via API.

<table id="biosample-registration" class="tg">
    <thead>
    <tr>
        <th class="tg-0lax">Use case #</th>
        <th class="tg-0lax">7</th>
    </tr>
    </thead>
    <tbody>
    <tr>
        <td class="tg-0lax">Name</td>
        <td class="tg-0lax">Biosample registration</td>
    </tr>
    <tr>
        <td class="tg-0lax">Actors</td>
        <td class="tg-0lax">
            <ul>
                <li>
                    BCDC? Sequencing portal?
                </li>
                <li>
                    Specimen portal
                </li>
            </ul>
        </td>
    </tr>
    <tr>
        <td class="tg-0lax">Description</td>
        <td class="tg-0lax">
            <ul>
                <li>
                    A lab has received their order of tissue and prepared libraries to be sent to the sequencing core. The biosamples need to be registered with the specimen portal to maintain the specimen heirarchy in one place.
                </li>
                <li>
                    Either the BCDC or sequencing portal service account updates specimen herirarchy in specimen portal. BICAN IDs are minted for lab generated biosamples IDs. Biosample IDs (both BICAN and lab generated) are associated to the appropriate specimen IDs from ordered tissue.
                </li>
            </ul>
    </tr>
    </tbody>
</table>

<table id="vocabulary-updates" class="tg">
<thead>
  <tr>
    <th class="tg-0lax">Use case #</th>
    <th class="tg-0lax">8</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0lax">Name</td>
    <td class="tg-0lax">Controlled Vocabulary updates</td>
  </tr>
  <tr>
    <td class="tg-0lax">Actors</td>
    <td class="tg-0lax">
      <ul>
        <li>
            Vocabulary services
        </li>
        <li>
            BCDC
        </li>
        <li>
            Specimen portal
        </li>
        <li>
            Sequencing tracker
        </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td class="tg-0lax">Description</td>
    <td class="tg-0lax">
        <ul>
            <li>
                A data submitter needs to request new controlled vocabulary terms for their project. They request the terms via the vocabulary services (details of where this system will lie TBD). Vocabulary services publish new term list to other systems so their forms can be updated to include new terms.
            </li>
        </ul>
  </tr>
</tbody>
</table>