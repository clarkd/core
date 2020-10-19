"""List of sensors and metadata, e.g.n name, device class, data path."""
from homeassistant.const import LENGTH_KILOMETERS, VOLUME_LITERS

SENSOR_TYPES = {
    "odometer": ["Odometer", "odometer.value", LENGTH_KILOMETERS],
    "fuel-level": ["Fuel Level", "fuel.fuelLevel", VOLUME_LITERS],
    "fuel-distance-to-empty": [
        "Fuel Distance to Empty",
        "fuel.distanceToEmpty",
        LENGTH_KILOMETERS,
    ],
    "battery": [
        "Battery Health",
        "battery.batteryHealth.value",
        None,
        {"voltage": "battery.batteryStatusActual.value"},
    ],
    "oil": [
        "Oil Life",
        "oil.oilLife",
        "Status",
        {"percent_remaining": "oil.oilLifeActual"},
    ],
    "tire-pressure": ["Tire Pressure (All)", "tirePressure.value", "Status"],
    "tire-pressure-left-front": [
        "Tire Pressure (Left Front)",
        "TPMS.leftFrontTireStatus.value",
        None,
        {"pressure_kpa": "TPMS.leftFrontTirePressure.value"},
    ],
    "tire-pressure-right-front": [
        "Tire Pressure (Right Front)",
        "TPMS.rightFrontTireStatus.value",
        None,
        {"pressure_kpa": "TPMS.rightFrontTirePressure.value"},
    ],
    "tire-pressure-left-rear-outer": [
        "Tire Pressure (Left Rear Outer)",
        "TPMS.outerLeftRearTireStatus.value",
        None,
        {"pressure_kpa": "TPMS.outerLeftRearTirePressure.value"},
    ],
    "tire-pressure-right-rear-outer": [
        "Tire Pressure (Right Rear Outer)",
        "TPMS.outerRightRearTireStatus.value",
        None,
        {"pressure_kpa": "TPMS.outerRightRearTirePressure.value"},
    ],
    "tire-pressure-left-rear-inner": [
        "Tire Pressure (Left Rear Inner)",
        "TPMS.innerLeftRearTireStatus.value",
        None,
        {"pressure_kpa": "TPMS.innerLeftRearTirePressure.value"},
    ],
    "tire-pressure-right-rear-inner": [
        "Tire Pressure (Right Rear Inner)",
        "TPMS.innerRightRearTireStatus.value",
        None,
        {"pressure_kpa": "TPMS.innerRightRearTirePressure.value"},
    ],
    "tire-pressure-recommended-front": [
        "Recommended Tire Pressure Front",  # PSI
        "TPMS.recommendedFrontTirePressure.value",
        "psi",
    ],
    "tire-pressure-recommended-rear": [
        "Recommended Tire Pressure Rear",  # PSI
        "TPMS.recommendedRearTirePressure.value",
        "psi",
    ],
}
