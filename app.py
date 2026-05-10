import streamlit as st

# Page Configuration
st.set_page_config(page_title="Mechanical Unit & Density Tool", layout="centered")

# Student Information Header
st.title("Mechanical Unit Converter & Material Density Checker")
st.markdown(f"""
**Name:** Idrees khan  
**Roll Number:** 25-ME-200  
---
""")

# Sidebar Navigation
option = st.sidebar.selectbox("Select Tool", ["Unit Converter", "Material Density Checker"])

if option == "Unit Converter":
    st.header("⚙️ Unit Converter")
    
    conv_type = st.selectbox("Conversion Type", ["Pressure", "Temperature", "Length"])
    
    col1, col2 = st.columns(2)
    
    if conv_type == "Pressure":
        with col1:
            val = st.number_input("Value in Pascal (Pa)", value=1.0)
        with col2:
            st.write(f"**PSI:** {val * 0.000145038:.4f}")
            st.write(f"**Bar:** {val / 100000:.5f}")
            st.write(f"**Atm:** {val / 101325:.5f}")

    elif conv_type == "Temperature":
        with col1:
            val = st.number_input("Value in Celsius (°C)", value=0.0)
        with col2:
            st.write(f"**Kelvin:** {val + 273.15:.2f} K")
            st.write(f"**Fahrenheit:** {(val * 9/5) + 32:.2f} °F")

    elif conv_type == "Length":
        with col1:
            val = st.number_input("Value in Meters (m)", value=1.0)
        with col2:
            st.write(f"**Millimeters:** {val * 1000:.2f} mm")
            st.write(f"**Inches:** {val * 39.3701:.2f} in")
            st.write(f"**Feet:** {val * 3.28084:.2f} ft")

elif option == "Material Density Checker":
    st.header("🔬 Material Density Database")
    
    # Common engineering materials
    materials = {
        "Steel": 7850,
        "Aluminum": 2700,
        "Copper": 8960,
        "Cast Iron": 7200,
        "Titanium": 4500,
        "Brass": 8500,
        "Water": 1000,
        "Concrete": 2400
    }
    
    selected_material = st.selectbox("Select a Material", list(materials.keys()))
    
    density = materials[selected_material]
    st.success(f"The density of **{selected_material}** is **{density} kg/m³**.")
    
    # Simple Mass Calculator
    st.subheader("Mass Calculator")
    volume = st.number_input("Enter Volume (m³)", min_value=0.0, value=1.0)
    mass = volume * density
    st.info(f"Calculated Mass: **{mass:,.2f} kg**")

st.markdown("---")
st.caption("Developed for Mechanical Engineering Applications")
