import streamlit as st

class UnitConverter:
    # Conversion factors relative to base units (meter for length, liter for volume)
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
        'picoliter': 1e-12
    }
    
    @staticmethod
    def convert(value, from_unit, to_unit):
        if from_unit not in UnitConverter.conversion_factors or to_unit not in UnitConverter.conversion_factors:
            raise ValueError(f"Unsupported unit: {from_unit} or {to_unit}")
        
        # Convert the value to the base unit (meter for length, liter for volume)
        base_value = value * UnitConverter.conversion_factors[from_unit]
        
        # Convert the base unit value to the target unit
        target_value = base_value / UnitConverter.conversion_factors[to_unit]
        
        return target_value

# Streamlit app
st.title('Unit Converter')

# Select conversion type
conversion_type = st.selectbox('Select conversion type', ['Length', 'Volume'])

if conversion_type == 'Length':
    units = ['meter', 'centimeter', 'millimeter', 'micrometer', 'nanometer']
elif conversion_type == 'Volume':
    units = ['liter', 'milliliter', 'microliter', 'nanoliter', 'picoliter']

# Select units and input value
from_unit = st.selectbox('From unit', units)
to_unit = st.selectbox('To unit', units)
value = st.number_input('Value to convert', min_value=0.0, format='%f')

if st.button('Convert'):
    converter = UnitConverter()
    result = converter.convert(value, from_unit, to_unit)
    st.write(f'{value} {from_unit} is {result} {to_unit}')

