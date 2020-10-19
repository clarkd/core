"""List of binary sensors and metadata, e.g. logo, data path, expected value."""
from homeassistant.components.binary_sensor import (
    DEVICE_CLASS_DOOR,
    DEVICE_CLASS_POWER,
    DEVICE_CLASS_WINDOW,
)

SENSOR_TYPES = {
    "alarm": ["Alarm", DEVICE_CLASS_POWER, "alarm.value", "NOTSET", "mdi:shield-car"],
    "window-driver": [
        "Driver's Window",  # Entity name
        DEVICE_CLASS_WINDOW,  # Entity class
        "windowPosition.driverWindowPosition.value",  # Path to data value (via coordinator)
        "Fully_Closed",  # Expected value for off position
    ],
    "window-passenger": [
        "Passenger's Window",
        DEVICE_CLASS_WINDOW,
        "windowPosition.passWindowPosition.value",
        "Fully_Closed",
    ],
    "window-driver-rear": [
        "Rear Driver's Window",
        DEVICE_CLASS_WINDOW,
        "windowPosition.rearDriverWindowPos.value",
        "Fully_Closed",
    ],
    "window-passenger-rear": [
        "Rear Passengers's Window",
        DEVICE_CLASS_WINDOW,
        "windowPosition.rearPassWindowPos.value",
        "Fully_Closed",
    ],
    "door-right-rear": [
        "Rear Passenger's Door",
        DEVICE_CLASS_DOOR,
        "doorStatus.rightRearDoor.value",
        "Closed",
        "mdi:car-door",
    ],
    "door-left-rear": [
        "Rear Driver's Door",
        DEVICE_CLASS_DOOR,
        "doorStatus.leftRearDoor.value",
        "Closed",
        "mdi:car-door",
    ],
    "door-driver": [
        "Driver's Door",
        DEVICE_CLASS_DOOR,
        "doorStatus.driverDoor.value",
        "Closed",
        "mdi:car-door",
    ],
    "door-passenger": [
        "Passenger's Door",
        DEVICE_CLASS_DOOR,
        "doorStatus.passengerDoor.value",
        "Closed",
        "mdi:car-door",
    ],
    "door-hood": [
        "Bonnet",
        DEVICE_CLASS_DOOR,
        "doorStatus.hoodDoor.value",
        "Closed",
        "mdi:car",
    ],
    "door-tailgate": [
        "Boot",
        DEVICE_CLASS_DOOR,
        "doorStatus.tailgateDoor.value",
        "Closed",
        "mdi:car-back",
    ],
    "door-tailgate-door": [
        "Boot (Inner)",
        DEVICE_CLASS_DOOR,
        "doorStatus.innerTailgateDoor.value",
        "Closed",
        "mdi:car-back",
    ],
    "ignition": [
        "Ignition",
        DEVICE_CLASS_POWER,
        "ignitionStatus.value",
        "Off",
        "mdi:engine",
    ],
}
