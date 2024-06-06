import streamlit as st

class UnitConverter:
    # Conversion factors relative to base units (meter for length, liter for volume, gram for weight, second for time)
    conversion_factors = {
        'meter': 1.0,
        'centimeter': 1e-2,
        'millimeter': 1e-3,
        'micrometer': 1e-6,
        'nanometer': 1e-9,
        'liter': 1.0,
        'milliliter': 1e-3,
        'microliter': 1e-6,
        'nanoliter': 1e-9,
        'picoliter': 1e-12,
        'gram': 1.0,
        'kilogram': 1e3,
        'milligram': 1e-3,
        'microgram': 1e-6,
        'second': 1.0,
        'minute': 60.0,
        'hour': 3600.0
    }
    
    @staticmethod
    def convert(value, from_unit, to_unit):
        if from_unit in ['celsius', 'fahrenheit', 'kelvin'] and to_unit in ['celsius', 'fahrenheit', 'kelvin']:
            return UnitConverter.convert_temperature(value, from_unit, to_unit)
        
        if from_unit not in UnitConverter.conversion_factors or to_unit not in UnitConverter.conversion_factors:
            raise ValueError(f"Unsupported unit: {from_unit} or {to_unit}")
        
        # Convert the value to the base unit
        base_value = value * UnitConverter.conversion_factors[from_unit]
        
        # Convert the base unit value to the target unit
        target_value = base_value / UnitConverter.conversion_factors[to_unit]
        
        return target_value
    
    @staticmethod
    def convert_temperature(value, from_unit, to_unit):
        if from_unit == 'celsius':
            if to_unit == 'fahrenheit':
                return (value * 9/5) + 32
            elif to_unit == 'kelvin':
                return value + 273.15
        elif from_unit == 'fahrenheit':
            if to_unit == 'celsius':
                return (value - 32) * 5/9
            elif to_unit == 'kelvin':
                return (value - 32) * 5/9 + 273.15
        elif from_unit == 'kelvin':
            if to_unit == 'celsius':
                return value - 273.15
            elif to_unit == 'fahrenheit':
                return (value - 273.15) * 9/5 + 32
        return value

# Streamlit app
st.title('Unit Converter')

# Select conversion type
conversion_type = st.selectbox('Select conversion type', ['Length', 'Volume', 'Weight', 'Time', 'Temperature'])

if conversion_type == 'Length':
    units = ['meter', 'centimeter', 'millimeter', 'micrometer', 'nanometer']
elif conversion_type == 'Volume':
    units = ['liter', 'milliliter', 'microliter', 'nanoliter', 'picoliter']
elif conversion_type == 'Weight':
    units = ['gram', 'kilogram', 'milligram', 'microgram']
elif conversion_type == 'Time':
    units = ['second', 'minute', 'hour']
elif conversion_type == 'Temperature':
    units = ['celsius', 'fahrenheit', 'kelvin']

# Select units and input value
from_unit = st.selectbox('From unit', units)
to_unit = st.selectbox('To unit', units)
value = st.number_input('Value to convert', format='%f')

if st.button('Convert'):
    converter = UnitConverter()
    result = converter.convert(value, from_unit, to_unit)
    st.write(f'{value} {from_unit} is {result} {to_unit}')
