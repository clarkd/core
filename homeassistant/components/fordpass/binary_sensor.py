"""Binary sensors for a Ford vehicle."""
from homeassistant.components.binary_sensor import BinarySensorEntity

from . import FordPassEntity
from .binary_sensor_types import SENSOR_TYPES
from .const import DOMAIN


async def async_setup_entry(hass, entry, async_add_entities):
    """Set up the sensors for doors, windows etc."""
    coordinator = hass.data[DOMAIN][entry.entry_id]

    async_add_entities(
        [
            FordPassBinarySensor(coordinator, key, *value)
            for key, value in SENSOR_TYPES.items()
        ]
    )


class FordPassBinarySensor(FordPassEntity, BinarySensorEntity):
    """Representation of a FordPass binary sensor."""

    def __init__(
        self,
        coordinator,
        key: str,
        name: str,
        device_class: str,
        path: str,
        value: str,
        icon=None,
    ):
        """Initialize sensor."""
        super().__init__(device_id=key, name=name, coordinator=coordinator)
        self._device_class = device_class
        self._path = path
        self._value = value
        self._icon = icon

    @property
    def device_class(self):
        """Return the class of the binary sensor."""
        return self._device_class

    @property
    def icon(self):
        """If available return a specific icon."""
        if self._icon is not None:
            return self._icon

    @property
    def is_on(self):
        """Compare the value at the given path to determine state."""
        return self.coordinator.data[self._path] != self._value
