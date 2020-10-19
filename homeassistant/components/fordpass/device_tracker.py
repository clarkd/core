"""Support for tracking Ford cars via FordPass."""
from homeassistant.components.device_tracker import SOURCE_TYPE_GPS
from homeassistant.components.device_tracker.config_entry import TrackerEntity

from . import DOMAIN, FordPassEntity


async def async_setup_entry(hass, entry, async_add_entities):
    """Set up the device trackers by config_entry."""
    coordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_entities([FordPassDeviceTracker(coordinator)])


class FordPassDeviceTracker(FordPassEntity, TrackerEntity):
    """A class representing a FordPass device tracker."""

    def __init__(self, coordinator):
        """Initialize tracker."""
        super().__init__(device_id="tracker", name="GPS", coordinator=coordinator)

    @property
    def latitude(self):
        """Return latitude value of the device."""
        return float(self.coordinator.data["gps.latitude"])

    @property
    def longitude(self):
        """Return longitude value of the device."""
        return float(self.coordinator.data["gps.longitude"])

    @property
    def source_type(self):
        """Return the source type, e.g. gps or router, of the device."""
        return SOURCE_TYPE_GPS

    @property
    def device_state_attributes(self):
        """Return the state attributes of the device."""
        attr = {}
        attr.update(
            {
                "gpsState": self.coordinator.data["gps.gpsState"],
                "status": self.coordinator.data["gps.status"],
                "timestamp": self.coordinator.data["gps.timestamp"],
            }
        )
        return attr
