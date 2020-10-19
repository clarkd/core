"""Sensors for a Ford vehicle."""
from homeassistant.helpers.entity import Entity

from . import FordPassEntity
from .const import DOMAIN
from .sensor_types import SENSOR_TYPES


async def async_setup_entry(hass, entry, async_add_entities):
    """Set up the sensors for fuel, pressure etc."""
    coordinator = hass.data[DOMAIN][entry.entry_id]

    async_add_entities(
        [
            FordPassSensor(coordinator, key, *value)
            for key, value in SENSOR_TYPES.items()
        ]
    )


class FordPassSensor(FordPassEntity, Entity):
    """Representation of a FordPass sensor."""

    def __init__(
        self,
        coordinator,
        key: str,
        name: str,
        path: str,
        unit_of_measurement: str,
        other_attributes=None,
    ):
        """Initialize sensor."""
        super().__init__(device_id=key, name=name, coordinator=coordinator)
        self._path = path
        self._unit_of_measurement = unit_of_measurement
        self._other_attributes = other_attributes

    @property
    def state(self):
        """Return the state of the sensor."""
        return self.coordinator.data[self._path]

    @property
    def unit_of_measurement(self):
        """Return the unit_of_measurement of the device."""
        return self._unit_of_measurement

    @property
    def device_state_attributes(self):
        """Return the state attributes of the device."""
        attrs = {}
        if self._other_attributes is not None:
            for name, path in self._other_attributes.items():
                try:
                    attrs[name] = self.coordinator.data[path]
                except KeyError:
                    pass  # Ignore key errors as it just means the data isn't available
        return attrs
