# pygdo-google-search

An optional PyGDO module boundary for web-search providers.

The initial module is API-neutral and inert: it does not send queries, scrape
Google result pages, store search terms, or require credentials. A concrete
provider must use an authorised search API, make its data handling explicit,
and be configured before it can issue requests.

## Installation

Clone the repository into `gdo/google_search`, then install it:

```sh
.venv/bin/python gdoadm.py install google_search
```

## Status

This initial release supplies the module boundary, localisation, and a
dependency test. Search-provider methods are intentionally deferred until the
chosen API and configuration are documented.

## Dependencies

- `net`

## License

Proprietary software licensed under the PyGDOv8 License.
