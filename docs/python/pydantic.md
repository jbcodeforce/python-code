# Pydantic

[Pydantic](https://docs.pydantic.dev/latest/) is a data validation library for Python, schema validation and serialization are controlled by type annotations.

Interesting constructs:

* [BaseSettings](https://docs.pydantic.dev/latest/api/pydantic_settings/#pydantic_settings.BaseSettings) Base class for settings, allowing values to be overridden by environment variables. Attention import pydantic_settings and install pydantic-settings
* [YamlConfigSettingsSource](https://docs.pydantic.dev/latest/api/pydantic_settings/#pydantic_settings.YamlConfigSettingsSource) get configuration from Yaml file