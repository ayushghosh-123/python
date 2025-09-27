import arrow
from collections import namedtuple

# Get the current UTC time and convert it to Europe/Rome timezone
brewing_time = arrow.utcnow().to("Europe/Rome")

# Define a namedtuple for chai profile
ChaiProfile = namedtuple("ChaiProfile", ["flavour", "aroma"])

chai = ChaiProfile(flavour="spicy", aroma="fragrant")
print(brewing_time)
print(chai)
