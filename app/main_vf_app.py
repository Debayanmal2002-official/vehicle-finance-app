import streamlit as st
import base64
import plotly.express as px
from pathlib import Path

# MAIN GLOBAL SETUP
st.set_page_config(
    page_title="ShiftGear Finance Advisor",
    page_icon="⚙️",
    layout="wide"
)
# Initialize session state for page navigation if it doesn't exist

if "vehicle_type" not in st.session_state:
    st.session_state.vehicle_type = None

# IMAGE DECODE AND ENCODE
def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except FileNotFoundError:
        return ""

BASE_DIR = Path(__file__).resolve().parents[1]
img_path = BASE_DIR / "assets" / "load_banner.png"
img_base64 = get_base64_image(img_path)

# ADD THEME AND HERO CSS

st.markdown(f"""
<style>
/* Import Premium Fonts from Google Fonts */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Plus+Jakarta+Sans:wght@700;800&display=swap');

/* App Background Adjustments */
.stApp {{
    background-color: #0F172A; 
    color: #F8FAFC;
    font-family: 'Inter', sans-serif; /* Changes global app text */
}}

/* Sidebar Theme Adjustment */
section[data-testid="stSidebar"] {{ 
    background-color: #1E293B;
}}
section[data-testid="stSidebar"] .stMarkdown, 
section[data-testid="stSidebar"] label {{
    color: #F8FAFC !important;
    font-family: 'Inter', sans-serif;
}}

/* Dynamic Hero Section with fallbacks */
.hero-section {{
    background-image: linear-gradient(rgba(15, 23, 42, 0.75), rgba(15, 23, 42, 0.85)), 
                      url("data:image/png;base64,{img_base64}");
    background-size: cover;
    background-position: center 80%;
    background-repeat: no-repeat;
    padding: 60px 45px; 
    border-radius: 18px;
    margin-bottom: 25px;
    border: 1px solid #334155;
    min-height: 200px; 
}}

.hero-title {{
    color: #F8FAFC; 
    font-family: 'Plus Jakarta Sans', sans-serif; /* High-end automotive brand vibe */
    font-size: 42px; 
    font-weight: 800; 
    margin-bottom: 12px; 
    letter-spacing: -1px; /* Tighter tracking for a premium feel */
    display: flex;
    align-items: center;
    gap: 12px; 
}}

.hero-subtitle {{
    color: #CBD5E1; 
    font-family: 'Inter', sans-serif;
    font-size: 16px; 
    font-weight: 400;
    max-width: 850px;
    line-height: 1.6;
    opacity: 0.95;
    letter-spacing: -0.1px;
}}

/* Force all markdown headers inside the workspace to use Plus Jakarta Sans */
h3, h2, h1 {{
    font-family: 'Plus Jakarta Sans', sans-serif !important;
}}

/* Force all input labels and form descriptions to use Inter sans-serif */
label[data-testid="stWidgetLabel"] p {{
    font-family: 'Inter', sans-serif !important;
    font-weight: 500 !important;
    color: #CBD5E1 !important; /* Makes the text labels a clean silver color */
}}

/* Force the actual numbers typed inside the boxes to look sharp and sans-serif */
input {{
    font-family: 'Inter', sans-serif !important;
    font-weight: 600 !important;
}}
</style>
""", unsafe_allow_html=True)
st.markdown(
                    """
                    <style>
                    div[data-testid="stNumberInput"] label {
                        color: #94A3B8 !important;
                        font-size: 13px !important;
                        font-family: 'Inter', sans-serif !important;
                        font-weight: 500 !important;
                        text-transform: uppercase !important;
                        letter-spacing: 0.5px !important;
                    }
                    div[data-testid="stNumberInput"] div[data-baseweb="input"] {
                        background-color: #1E293B !important;
                        border: 1px solid #334155 !important;
                        border-radius: 12px !important;
                        padding: 5px 10px !important;
                    }
                    div[data-testid="stNumberInput"] input {
                        color: #F8FAFC !important;
                        font-size: 32px !important;
                        font-family: 'Plus Jakarta Sans', sans-serif !important;
                        font-weight: 800 !important;
                    }
                    </style>
                    """,
                    unsafe_allow_html=True
                )

def create_kpi_card(title, value, text_color="#F8FAFC", bg_style="background-color: #1E293B; border: 1px solid #334155;"):
    """
    Generates a ultra-premium, universally responsive HTML KPI card.
    - title: The label at the top of the card
    - value: The main numeric value (e.g., ₹15,432)
    - text_color: Hex code for the primary number color
    - bg_style: Custom CSS string for special card backgrounds/gradients
    """
    return f"""
    <div style="{bg_style} padding: 22px 25px; border-radius: 12px; margin-bottom: 15px;">
        <div style="color: #94A3B8; font-size: 13px; font-family: 'Inter', sans-serif; font-weight: 500; text-transform: uppercase; letter-spacing: 0.5px;">
            {title}
        </div>
        <div style="color: {text_color}; font-size: 32px; font-family: 'Plus Jakarta Sans', sans-serif; font-weight: 800; margin-top: 5px;">
            {value}
        </div>
    </div>
    """
def render_operator(symbol):
    """
    Renders a perfectly vertically-centered operator (+ or =)
    to match the exact height and alignment of the ultra-premium cards.
    """
    st.markdown(
        f"""
        <div style="
            display: flex; 
            align-items: center; 
            justify-content: center; 
            height: 104px; 
            font-size: 32px; 
            font-family: 'Plus Jakarta Sans', sans-serif; 
            font-weight: 700; 
            color: #64748B;
            margin-bottom: 15px;
        ">
            {symbol}
        </div>
        """,
        unsafe_allow_html=True
    )

## -- Conditional Page Rendering -- ##

if st.session_state.vehicle_type is None:
    # LANDING PAGE: Vehicle Selection Title
    st.markdown("""
    <div class="hero-section">
        <div class="hero-title"> ShiftGear Finance Advisor </div>
        <div class="hero-subtitle">
            <i>Don't get stalled by bad dealership math. Calculate your true cost of ownership before you sign.</i>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown(
        "<h3 style='text-align: center; font-family: \"Plus Jakarta Sans\", sans-serif; margin-bottom: 30px;'>Select Your Asset Type to Begin</h3>",
        unsafe_allow_html=True)
    st.markdown("""
            <style>
            /* Base configuration for our custom card buttons */
            div[class*="st-key-"] button {
                height: 220px !important;
                width: 100% !important;
                border-radius: 15px !important;
                border: 1px solid #334155 !important;
                color: #F8FAFC !important;
                font-family: 'Plus Jakarta Sans', sans-serif !important;
                font-size: 22px !important;
                font-weight: 700 !important;
                transition: all 0.3s ease-in-out !important;
                background-size: cover !important;
                background-position: center !important;
                display: flex !important;
                flex-direction: column !important;
                justify-content: center !important;
                align-items: center !important;
                white-space: pre-wrap !important; /* Forces our subtitle line breaks to render cleanly */
                box-shadow: inset 0 0 0 2000px rgba(15, 23, 42, 0.85) !important; /* Dark tint overlay */
            }

            /* Apply individual background images using native Streamlit auto-key classes */
            div[class*="st-key-bike_select"] button {
                background-image: url('https://images.unsplash.com/photo-1664643890508-05223aa7f580?q=80&w=1170&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D') !important;
                height: 220px !important;
                width: 100% !important;
                border-radius: 15px !important;
                border: 1px solid #334155 !important;
                color: #F8FAFC !important;
                font-family: 'Plus Jakarta Sans', sans-serif !important;
                font-size: 28px !important;       /* Made the text larger and sharper */
                font-weight: 800 !important;       /* Extra bold for that premium look */
                letter-spacing: 2px !important;    /* Elegant spacing between letters */
                text-transform: uppercase !important; /* Clean, modern uppercase look */
                transition: all 0.3s ease-in-out !important;
                background-size: cover !important;
                background-position: center !important;
                display: flex !important;
                justify-content: center !important;
                align-items: center !important;
                box-shadow: inset 0 0 0 2000px rgba(15, 23, 42, 0.8) !important;
            }

            div[class*="st-key-car_select"] button {
                background-image: url('https://images.unsplash.com/photo-1594070319944-7c0cbebb6f58?q=80&w=1100&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D') !important;
            }

            /* Premium Hover Glow and Lift Effects */
            div[class*="st-key-"] button:hover {
                transform: translateY(-5px) !important;
                border-color: #6366F1 !important;
                box-shadow: inset 0 0 0 2000px rgba(15, 23, 42, 0.65), 0 10px 25px -5px rgba(99, 102, 241, 0.4) !important;
                color: #FFFFFF !important;
            }
            </style>
            """, unsafe_allow_html=True)

    # 2. Render the columns cleanly with single-word high-end labels
    col1, col2 = st.columns(2)

    with col1:
        if st.button("MOTO", key="bike_select", use_container_width=True):
            st.session_state.vehicle_type = "Bike"
            st.rerun()

    with col2:
        if st.button("AUTO", key="car_select", use_container_width=True):
            st.session_state.vehicle_type = "Car"
            st.rerun()

else:
    # ----------------------------------------------------
    # BRANCH 1: COMPLETE MOTO (BIKE) TERMINAL ENVIRONMENT
    # ----------------------------------------------------
    if st.session_state.vehicle_type == "Bike":
        with st.sidebar:

            if st.button("← Reselect Asset", key="nav_bike_back", use_container_width=True):
                st.session_state.vehicle_type = None
                st.rerun()

            st.markdown("### 🛠️ Bike Financial Levers")
            bike_price = st.number_input("Bike On Road Price (₹)", min_value=50000, max_value=8000000, value=180000,
                                         step=10000, key="sl_bike_p")
            bike_rate = st.number_input("Bike Interest Rate (Annual %)", min_value=3.0, max_value=18.0, value=14.0,
                                        step=0.25, key="sl_bike_r")
            bike_down_p = st.number_input("Down Payment (₹)", min_value=0, max_value=int(bike_price), value=18000,
                                          step=2000, key="sl_bike_dp", help = "For Basic Loan Breakdown tab only, won't effect rest tabs")
            bike_tenure = st.number_input("Tenure Duration (Years)", min_value=1, max_value=5, value=5, step=1,
                                          key="sl_bike_t", help = "For Basic Loan Breakdown tab only, won't effect rest tabs")
            # 📑 Native Browser PDF Print Trigger
st.markdown("### 🖨️ Export Financial Analysis")

# Centered layout container for the custom print trigger
p_col1, p_col2, p_col3 = st.columns([1, 2, 1])

with p_col2:
    # Custom HTML button that fires window.print() on click
    print_button_html = """
    <button onclick="window.print()" style="
        width: 100%;
        background-color: #38BDF8;
        color: #0F172A;
        border: none;
        padding: 12px 24px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        font-weight: bold;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 8px;
        transition-duration: 0.2s;
        box-shadow: 0 4px 6px -1px rgba(56, 189, 248, 0.2);
    " onmouseover="this.style.backgroundColor='#0EA5E9'" onmouseout="this.style.backgroundColor='#38BDF8'">
        📄 Generate & Download PDF Report
    </button>
    """
    st.components.v1.html(print_button_html, height=60)

            # Pure Bike Mathematical Formulas
            bike_loan_principal = bike_price - bike_down_p
            bike_months = bike_tenure * 12
            bike_monthly_rate = (bike_rate / 12) / 100
            if bike_monthly_rate > 0:
                bike_emi = (bike_loan_principal * bike_monthly_rate * (1 + bike_monthly_rate) ** bike_months) / (
                        (1 + bike_monthly_rate) ** bike_months - 1)
            else:
                bike_emi = bike_loan_principal / bike_months

            bike_total_payout = bike_emi * bike_months
            bike_total_interest = bike_total_payout - bike_loan_principal
            bike_burden_ratio = (bike_total_interest / bike_price) * 100


        st.markdown("""
        <div style="
            position: relative; 
            background-image: linear-gradient(to right, rgba(15, 23, 42, 0.95) 40%, rgba(15, 23, 42, 0.3)), 
                              url('https://images.unsplash.com/photo-1768921646736-f8793b0b5507?q=80&w=1170&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'); 
            background-size: cover; background-position: 100% 80%; padding: 35px 40px; border-radius: 16px; margin-bottom: 25px; border: 1px solid #334155;
        ">
            <span style="background-color: #6366F122; color: #6366F1; padding: 4px 12px; border-radius: 20px; font-size: 11px; font-weight: 700; letter-spacing: 1.5px; text-transform: uppercase; border: 1px solid #6366F144;">
                Two-Wheeler Terminal Active
            </span>
            <h1 style="margin: 10px 0 4px 0; font-family: 'Plus Jakarta Sans', sans-serif; font-size: 32px; font-weight: 800; color: #F8FAFC; letter-spacing: -0.5px;">
                MOTO INTELLIGENCE
            </h1>
            <p style="margin: 0; color: #94A3B8; font-family: 'Inter', sans-serif; font-size: 14px;">
                Optimize your custom superbike, commuter, or scooter loan dynamics.
            </p>
        </div>
        """, unsafe_allow_html=True)

        tab_bike_basic, tab_bike_operating ,tab_bike_optimal = st.tabs(["📊 Basic Loan Breakdown", "📉Operating Cost", "⚡ Optimal Finance Plan"])

        with tab_bike_basic:

            # 1C. Completely Separate Bike Column Grid
            col_outputs_bike_d, col_outputs_bike_i = st.columns([1, 1.2], gap="large")

            with col_outputs_bike_d:

                # 1. Standard Slate Card with Electric Indigo Text
                card_emi = create_kpi_card(
                    title="Estimated Monthly Payout (EMI)",
                    value=f"₹{int(bike_emi):,}",
                    text_color="#6366F1"
                )

                # 2. Special Green Highlight Card with Custom Gradient Background
                card_total = create_kpi_card(
                    title="Total Effective Loan",
                    value=f"₹{int(bike_total_payout):,}",
                    text_color="#F8FAFC",
                    bg_style="background-color: #1E293B; border: 1px solid #22C55E44; background-image: linear-gradient(to right, #1E293B, #14532D22);"
                )

                # 3. Standard Slate Card with Silver White Text
                card_interest = create_kpi_card(
                    title="Total Interest Amount",
                    value=f"₹{int(bike_total_interest):,}",
                    text_color="#F8FAFC"
                )

                # 4. The Financial Friction / Burden Ratio Card
                card_burden = create_kpi_card(
                    title="Total Outflow Interest Leakage",
                    value=f"{bike_burden_ratio:.1f}%",
                    text_color="#F43F5E"  # High-end Coral Warning Red
                )

                # Render all three cards to the screen cleanly
                st.markdown(card_emi  + card_total + card_interest + card_burden, unsafe_allow_html=True)

            with col_outputs_bike_i:
                with st.container(border=True):
                    chart_view_bike = st.radio(
                        "Select Visualization Horizon",
                        options=["Total Lifetime", "Yearly Breakdown"],
                        horizontal=True,
                        key="view_bike",
                        label_visibility="collapsed"
                    )
                    # Generate list of years dynamically based on user's input tenure
                    bike_year_options = [f"Year {i}" for i in range(1, int(bike_tenure) + 1)]

                    # CASE A: TOTAL LIFETIME COST RING
                    if chart_view_bike == "Total Lifetime":
                        bike_labels = ['Principal Loan Amount', 'Total Interest Cost']
                        bike_values = [int(bike_loan_principal), int(bike_total_interest)]
                        selected_bike_year_str = st.selectbox("Select Target Year Analysis", options="NA",
                                                              key="sb_bike_yr")
                        chart_title = "Lifetime Cost Matrix"

                    # CASE B: YEARLY DRILLDOWN CHARTS
                    else:
                        selected_bike_year_str = st.selectbox("Select Target Year Analysis", options=bike_year_options,
                                                              key="sb_bike_yr")
                        selected_bike_year = int(selected_bike_year_str.split()[-1])

                        # Math to calculate specific year's interest and principal using amortization loop
                        remaining_balance = bike_loan_principal
                        year_interest = 0
                        year_principal = 0

                        # Calculate amortization scheduling month by month up to target year
                        for m in range(1, int(bike_months) + 1):
                            current_month_interest = remaining_balance * bike_monthly_rate
                            current_month_principal = bike_emi - current_month_interest
                            remaining_balance -= current_month_principal

                            # If this month falls inside our target year, log it!
                            if ((m - 1) // 12) + 1 == selected_bike_year:
                                year_interest += current_month_interest
                                year_principal += current_month_principal

                        bike_labels = [f'{selected_bike_year_str} Principal Paid', f'{selected_bike_year_str} Interest Cost']
                        bike_values = [int(year_principal), int(year_interest)]
                        chart_title = f"{selected_bike_year_str} Repayment Breakdown"

                    # Render the dynamic Plotly ring based on selected logic state
                    fig_bike = px.pie(
                        names=bike_labels,
                        values=bike_values,
                        hole=0.6,
                        color_discrete_sequence=['#15803D', '#B91C1C']
                    )

                    fig_bike.update_layout(
                        title=dict(text=chart_title, x=0.5, y=0.95, font=dict(size=14, weight='bold', color='#94A3B8')),
                        margin=dict(t=50, b=20, l=10, r=10),
                        showlegend=True,
                        legend=dict(orientation="h", yanchor="bottom", y=-0.1, xanchor="center", x=0.5),
                        paper_bgcolor="rgba(0,0,0,0)",
                        plot_bgcolor="rgba(0,0,0,0)",
                        font=dict(family="Inter, sans-serif", color="#F8FAFC", size=13)
                    )

                    fig_bike.update_traces(
                        hovertemplate="<b>%{label}</b><br>Amount: ₹%{value:,}<br>Percentage: %{percent}<extra></extra>",
                        textinfo='percent',
                        textfont=dict(size=14, weight='bold', color='#FFFFFF')
                    )

                    st.plotly_chart(fig_bike, use_container_width=True, config={'displayModeBar': False})

        with tab_bike_operating:
            st.write("")  # Clear structural spacer

            # Segmented structural picker at the top
            propulsion_type = st.radio(
                "Select Vehicle Engine Variant",
                options=["Fuel (Petrol)", "Electric (EV)"],
                horizontal=True,
                key="b_propulsion_toggle",
                label_visibility="collapsed"
            )
            st.write("")

            # ----------------------------------------------------
            # CONDITION A: FUEL (PETROL) CALCULATION BLOCK
            # ----------------------------------------------------
            if propulsion_type == "Fuel (Petrol)":
                col_op_inputs_l, col_op_inputs_r = st.columns(2, gap="medium")

                with col_op_inputs_l:
                    st.markdown("##### 🌆 City Commute Split")
                    b_weekly_city_km = st.number_input("Weekly City Distance (km)", min_value=0, max_value=2000, value=150,
                                                      step=5, key="b_fuel_cc_km")
                    b_city_mileage = st.number_input("City Mileage (km/L)", min_value=1, max_value=90, value=40,
                                                     step=2, key="b_fuel_cc_mlg")

                with col_op_inputs_r:
                    st.markdown("##### 🛣️ Highway Commute Split")
                    b_weekly_hwy_km = st.number_input("Weekly Highway Distance (km)", min_value=0, max_value=1500,
                                                      value=100, step=20, key="b_fuel_hw_km")
                    b_hwy_mileage = st.number_input("Highway Mileage (km/L)", min_value=1, max_value=95, value=52,
                                                    step=2, key="b_fuel_hw_mlg")
                st.markdown("##### 🛠️ Fixed Maintenance Overhead")
                col1, col2, col3 = st.columns(3)
                with col1:
                    b_fuel_price = st.number_input("Local Petrol Price (₹/L)", min_value=60.0, max_value=1000.0,
                                                   value=104.5, step=0.5, key="b_fuel_price_val")
                with col2:
                    b_annual_service = st.number_input("Annual Servicing Costs (₹)", min_value=100, max_value=100000,
                                                       value=5500, step=100, key="b_fuel_srv")
                with col3:
                    b_annual_od_ins = st.number_input("Annual Insurance Renewal (₹)", min_value=100,
                                                      max_value=100000, value=1600, step=100, key="b_fuel_ins")

                # Petrol Processing Engine Math
                b_monthly_city_dist = b_weekly_city_km * 4.33
                b_monthly_hwy_dist = b_weekly_hwy_km * 4.33
                b_total_monthly_dist = b_monthly_city_dist + b_monthly_hwy_dist

                b_fuel_city_liters = b_monthly_city_dist / b_city_mileage if b_city_mileage > 0 else 0
                b_fuel_hwy_liters = b_monthly_hwy_dist / b_hwy_mileage if b_hwy_mileage > 0 else 0
                b_total_fuel_liters = b_fuel_city_liters + b_fuel_hwy_liters

                b_true_efficiency = b_total_monthly_dist / b_total_fuel_liters if b_total_fuel_liters > 0 else 0
                b_monthly_running_cost = b_total_fuel_liters * b_fuel_price
                b_monthly_fixed_overhead = (b_annual_service + b_annual_od_ins) / 12

                efficiency_display_str = f"{b_true_efficiency:.1f} km/L"
                sub_caption_str = f"Total Fuel Burned: {b_total_fuel_liters:.1f} Liters/mo"

            # ----------------------------------------------------
            # CONDITION B: ELECTRIC (EV) CALCULATION BLOCK
            # ----------------------------------------------------
            else:
                col_op_inputs_l, col_op_inputs_r = st.columns(2, gap="medium")

                with col_op_inputs_l:
                    st.markdown("##### 🌆 City Electric Split")
                    b_weekly_city_km = st.number_input("Weekly City Distance (km)", min_value=0, max_value=200, value=150,
                                                      step=5, key="b_ev_cc_km")
                    b_city_efficiency = st.number_input("City Range Efficiency (km/kWh)", min_value=5, max_value=120,
                                                        value=31, step=2, key="b_ev_cc_eff")

                with col_op_inputs_r:
                    st.markdown("##### 🛣️ Highway Electric Split")
                    b_weekly_hwy_km = st.number_input("Weekly Highway Distance (km)", min_value=0, max_value=1500,
                                                      value=100, step=20, key="b_ev_hw_km")
                    b_hwy_efficiency = st.number_input("Highway Range Efficiency (km/kWh)", min_value=5, max_value=120,
                                                       value=19, step=2, key="b_ev_hw_eff")
                st.markdown("##### 🛠️ EV Maintenance Overhead")


                col1, col2, col3 = st.columns(3)
                with col1:
                    b_elec_rate = st.number_input("Electricity Cost (₹/Unit per kWh)", min_value=1.0, max_value=100.0,
                                                  value=10.5, step=0.5, key="b_ev_elec_rate")
                with col2:
                    b_annual_service = st.number_input("Annual EV Inspection/Brakes (₹)", min_value=200,
                                                       max_value=20000, value=1200, step=200, key="b_ev_srv")
                with col3:
                    b_annual_od_ins = st.number_input("Annual Own Damage Insurance Renewal (₹)", min_value=200,
                                                      max_value=12000, value=1850, step=100, key="b_ev_ins")

                # EV Processing Engine Math
                b_monthly_city_dist = b_weekly_city_km * 4.33
                b_monthly_hwy_dist = b_weekly_hwy_km * 4.33
                b_total_monthly_dist = b_monthly_city_dist + b_monthly_hwy_dist

                b_energy_city_kwh = b_monthly_city_dist / b_city_efficiency if b_city_efficiency > 0 else 0
                b_energy_hwy_kwh = b_monthly_hwy_dist / b_hwy_efficiency if b_hwy_efficiency > 0 else 0
                b_net_energy_stored = b_energy_city_kwh + b_energy_hwy_kwh

                # Incorporating standard 10% structural loss factor on charger wall pull
                b_total_billed_units = b_net_energy_stored * 1.10

                b_true_efficiency = b_total_monthly_dist / b_total_billed_units if b_total_billed_units > 0 else 0
                b_monthly_running_cost = b_total_billed_units * b_elec_rate
                b_monthly_fixed_overhead = (b_annual_service + b_annual_od_ins) / 12

                efficiency_display_str = f"{b_true_efficiency:.1f} km/kWh"
                sub_caption_str = f"Meter Load: {b_total_billed_units:.1f} Units (incl. 10% loss)"

            # ----------------------------------------------------
            # UNIFIED METRIC RENDER PIPELINE
            # ----------------------------------------------------
            b_total_monthly_operating = b_monthly_running_cost + b_monthly_fixed_overhead
            b_total_monthly_outflow = b_total_monthly_operating + bike_emi

            st.markdown("---")
            st.markdown("### 📊 Operational Cost Matrix")

            col_op_m1, col_op_m2, col_op_m3, col_op_m4 = st.columns(4)

            with col_op_m1:
                card_running_ops = create_kpi_card(
                    title="Monthly Running Outflow",
                    value=f"₹{int(b_monthly_running_cost):,}",
                    text_color="#6366F1"
                )
                st.markdown(card_running_ops, unsafe_allow_html=True)
                st.caption(f"Monthly Travel Range: {int(b_total_monthly_dist):,} km")

            with col_op_m2:
                card_efficiency_ops = create_kpi_card(
                    title="True Blended Efficiency",
                    value=efficiency_display_str,
                    text_color="#F8FAFC"
                )
                st.markdown(card_efficiency_ops, unsafe_allow_html=True)
                st.caption(sub_caption_str)

            with col_op_m3:
                card_total_ops = create_kpi_card(
                    title="Total Monthly Operating Cost",
                    value=f"₹{int(b_total_monthly_operating):,}",
                    text_color="#38BDF8",
                    bg_style="background-color: #1E293B; border: 1px solid #38BDF844; background-image: linear-gradient(to right, #1E293B, #0369A111);"
                )
                st.markdown(card_total_ops, unsafe_allow_html=True)
                st.caption(f"Fixed Maintenance Base: ₹{int(b_monthly_fixed_overhead):,}/mo")

            with col_op_m4:
                card_total_out = create_kpi_card(
                    title="Total Monthly Outflow",
                    value=f"₹{int(b_total_monthly_outflow):,}",
                    text_color="#38BDF8",
                    bg_style="background-color: #1E293B; border: 1px solid #38BDF844; background-image: linear-gradient(to right, #1E293B, #0369A111);"
                )
                st.markdown(card_total_out, unsafe_allow_html=True)
                st.caption(f"Includes Loan EMI: ₹{int(bike_emi):,}/mo")

        with tab_bike_optimal:

            col_savings, col_equal, col_burden, col_plus, col_emi = st.columns([5, 1, 5, 1, 3.5])

            with col_savings:
                st.write("")
                b_m_savings = st.number_input(
                    label="Monthly Comfortable Savings",
                    value=int(b_total_monthly_outflow),
                    step=500,
                    label_visibility="visible",
                    help = "Ideally less than 10% of user's Monthly Net Income, can be stretched to 15%. More than 15% is financially Risky."
                )

            # Column 2: The Equal Sign
            with col_equal:
                render_operator("=")

            # Column 3: Total Operating Burden Card
            with col_burden:
                st.markdown(
                    create_kpi_card(
                        title="Total Monthly Operating Cost",
                        value=f"₹{int(b_total_monthly_operating):,}"
                    ),
                    unsafe_allow_html=True
                )

            # Column 4: The Plus Sign (Replacing the rogue dot)
            with col_plus:
                render_operator("+")

            mx_emi = b_m_savings - b_total_monthly_operating

            # Column 5: Max Allowable EMI Card
            with col_emi:
                st.markdown(
                    create_kpi_card(
                        title="Max Allowable EMI",
                        value=f"₹{int(mx_emi):,}"
                    ),
                    unsafe_allow_html=True
                )
            # Dynamic Dropdown Explanation Section for Bike
            with st.expander("💡 The Financial Beta Test Strategy (Logic Behind This Equation)"):
                st.markdown(f"""
                                ### 🧪 The Sandbox Ownership Simulation
                                This matrix doesn't just calculate affordability—it **stress-tests your behavior** before you sign a legally binding bank contract.

                                ---

                                ### 🎯 Why This Strategy is Bulletproof:

                                * **🛡️ Zero Lifestyle Shock**
                                  You adjust to the financial strain *before* the vehicle arrives. 
                                  * **Before Purchase:** **₹{int(b_m_savings):,}/mo** flows entirely into your **Savings Pool**.
                                  * **After Purchase:** That exact same **₹{int(b_m_savings):,}/mo** splits into **₹{int(b_total_monthly_operating):,}** (Fuel/Service) + **₹{int(mx_emi):,}** (Bank EMI). 
                                  * *Net lifestyle impact:* **Identical.** Only the direction of the cash flow changes.

                                * **🛑 Safe Sabotage Buffer**
                                  If a life emergency hits in Month 3 and breaks your budget, **nothing bad happens**. No missed bank EMIs, no ruined credit score, no repossession trucks. You simply reset the simulation.

                                * **⚙️ Self-Correcting Down Payment Engine**
                                  If the bike's price tag breaches your current budget, you don't give up. You just run the beta test longer. The capital stacking up in your sandbox account naturally inflates your **Down Payment**, crushing the future loan principal down until it fits your rule perfectly.

                                ---

                                > **⚠️ The Ultimate Rule:** If you cannot comfortably survive the mock outflow of **₹{int(b_m_savings):,}/mo** during this simulation phase, your life isn't ready for the vehicle yet. Let the simulation protect your wealth.
                                """)
            st.markdown("---")
            st.markdown("### ⚡ Short-Term Purchase Runway", help = "Vehicle prices may increase over time due to inflation and market conditions."
                                                                   " This calculator does not predict future on-road price inflation "
                                                                   "because long-term pricing is highly unpredictable.\n\n"
                                                                   " The projection assumes your short-term vehicle savings are parked in instruments such as:\n"
                                                                   " 1) High-return mutual funds\n"
                                                                   " 2) Liquid/arbitrage funds\n"
                                                                   " 3) Recurring deposits (RDs).\n\n"
                                                                   "Historically, these often generate returns that partially or fully "
                                                                   "offset average vehicle inflation over shorter ownership timelines.")

            # 1. User Choice for Aggressive Short Tenure Horizon
            b_test_tenure = st.selectbox(
                "Select Beta Test Tenure Strategy",
                options=[1, 1.5, 2, 2.5, 3],
                format_func=lambda x: f"{x} Year Plan ({int(x * 12)} Months)",
                key="b_beta_tenure_pick",
                help = "Loan tenure after the Down-Payment. Ideally less than 2 years, max 3 years."
            )

            # 2. Mathematical Calculations Pipeline
            b_test_months = b_test_tenure * 12

            # Deriving the monthly interest rate from your main sidebar lever (bike_rate)
            b_test_monthly_rate = (bike_rate / 12) / 100

            # Reverse compounding engine: Calculate actual max loan principal capacity

            b_max_principal_loan = mx_emi * (
                    ((1 + b_test_monthly_rate) ** b_test_months - 1) /
                    (b_test_monthly_rate * (1 + b_test_monthly_rate) ** b_test_months)
            )

            b_total_loan_capacity = mx_emi * b_test_months

            # 20% Asset Valuation Boundary Floor
            b_cash_floor_limit = bike_price * 0.20

            # ----------------------------------------------------
            # SCENARIO A: FINANCING IS TRIVIAL -> GO FOR FULL DOWN
            # ----------------------------------------------------
            if b_total_loan_capacity < b_cash_floor_limit or b_max_principal_loan < 30000:
                st.success("### 🎉 Strategy Recommendation: GO FOR FULL DOWN PAYMENT")

                # Calculate timeline to buy it outright with 100% cash
                b_months_to_full_cash = bike_price / b_m_savings if b_m_savings > 0 else 0

                rejection_reason = ""
                if b_max_principal_loan < 30000:
                    rejection_reason = f"Your maximum borrowable principal (**₹{int(b_max_principal_loan):,}**) falls below the real-world banking threshold of **₹30,000**. No major lender will approve a vehicle loan this low."
                else:
                    rejection_reason = f"Your true borrowable principal capacity (**₹{int(b_max_principal_loan):,}**) falls beneath 20% of the vehicle's sticker value (**₹{int(b_cash_floor_limit):,}**). Taking a loan for this small an amount is an inefficient capital drain."

                st.markdown(f"""
                        {rejection_reason}

                        * **Strategic Direction:** Avoid all banking friction, hidden processing fees, and interest leakage.
                        * **Beta Test Target:** Accumulate 100% cash to buy the asset outright.
                        * **Time to Destination:** Approximately **{b_months_to_full_cash:.1f} months** of running your current savings rate of **₹{int(b_m_savings):,}/mo**.
                        """)

            # ----------------------------------------------------
            # SCENARIO B: CALCULATE MINIMUM DOWN PAYMENT & TIMELINE
            # ----------------------------------------------------
            else:
                st.warning("### 📈 Strategy Recommendation: STRUCTURED DOWN PAYMENT PLAN")

                b_min_down_payment = bike_price - b_max_principal_loan
                b_months_to_full_cash = bike_price / b_m_savings

                if b_max_principal_loan >= bike_price:
                    b_min_down_payment = 0.0
                    b_time_to_down_payment = 0.0
                    b_actual_loan_needed = bike_price
                else:
                    b_min_down_payment = bike_price - b_max_principal_loan
                    b_time_to_down_payment = b_min_down_payment / b_m_savings if b_m_savings > 0 else 0
                    b_actual_loan_needed = b_max_principal_loan

                # Render Layout Split
                b_col_d1, b_col_d2, b_col_d3 = st.columns(3)

                with b_col_d1:
                    card_min_dp = create_kpi_card(
                        title="Required Target Down Payment",
                        value=f"₹{int(b_min_down_payment):,}",
                        text_color="#3B6896"  # Rose warning/target indicator
                    )
                    st.markdown(card_min_dp, unsafe_allow_html=True)
                    st.caption(f"Bridges the gap for a max ₹{int(b_total_loan_capacity):,} loan package.")

                with b_col_d2:
                    card_time_dp = create_kpi_card(
                        title="Savings Duration",
                        value=f"{b_time_to_down_payment:.1f} Months",
                        text_color="#22C55E"  # Success green timeline
                    )
                    st.markdown(card_time_dp, unsafe_allow_html=True)
                    st.caption(f"Months required at a save rate of ₹{int(b_m_savings):,}/mo.")

                with b_col_d3:
                    total_interest_dp = create_kpi_card(
                        title="Total Interest Paid",
                        value=f"₹{int(b_total_loan_capacity - b_max_principal_loan):,}",
                        text_color="#F43F5E"
                    )
                    st.markdown(total_interest_dp, unsafe_allow_html=True)
                    st.caption(f"Extra {int(((b_total_loan_capacity - b_max_principal_loan)/bike_price)*100):,}% than actual Initial on Road Price.")

                st.markdown(f"""
                    ### 🎯 Beta Test Action Plan

                    * **🛠️ The Sandbox Routine:** Lock down and divert **₹{int(b_m_savings):,}/mo** into your simulation pool.
                    * **⏳ Testing Timeline:** Run this drill for exactly **{b_time_to_down_payment:.1f} Months**.
                    * **💰 Target Down Payment:** Once your pool hits **₹{int(b_min_down_payment):,}**, sign the paperwork. Your daily lifestyle won't shift a single millimeter.

                    ---

                    ### ⚡ The Time-vs-Money Trade-Off:
                    * **🚀 Time Saved:** You hit the road **{(b_months_to_full_cash - b_time_to_down_payment):.1f} Months earlier** than waiting to buy the vehicle with 100% full cash down.
                    * **🏆 Asset Ownership:** You will 100% own the vehicle **{(bike_months - b_time_to_down_payment - b_test_months ):.1f} Months** before the initial **{int(bike_tenure):,} Years** loan.
                    * **💸 Premium Paid:** The total interest cost for skipping time is just **₹{int(b_total_loan_capacity - b_max_principal_loan):,}** extra.
                    """)



    # ----------------------------------------------------
    # BRANCH 2: COMPLETE AUTO (CAR) TERMINAL ENVIRONMENT
    # ----------------------------------------------------
    elif st.session_state.vehicle_type == "Car":
        with st.sidebar:

            if st.button("← Reselect Asset", key="nav_car_back", use_container_width=True):
                st.session_state.vehicle_type = None
                st.rerun()

            st.markdown("### 🛠️ Car Financial Levers")
            car_price = st.number_input("Car On Road Price (₹)", min_value=300000, max_value=7500000, value=1800000,
                                        step=50000, key="sl_car_p")
            car_rate = st.number_input("Car Interest Rate (Annual %)", min_value=3.0, max_value=18.0, value=9.00,
                                       step=0.25, key="sl_car_r")
            car_down_p = st.number_input("Down Payment (₹)", min_value=0, max_value=int(car_price), value=180000,
                                         step=10000, key="sl_car_dp", help = "For Basic Loan Breakdown tab only, won't effect rest tabs")
            car_tenure = st.number_input("Tenure Duration (Years)", min_value=1, max_value=7, value=7, step=1,
                                         key="sl_car_t", help = "For Basic Loan Breakdown tab only, won't effect rest tabs")
            # 📑 Native Browser PDF Print Trigger
st.markdown("### 🖨️ Export Financial Analysis")

# Centered layout container for the custom print trigger
p_col1, p_col2, p_col3 = st.columns([1, 2, 1])

with p_col2:
    # Custom HTML button that fires window.print() on click
    print_button_html = """
    <button onclick="window.print()" style="
        width: 100%;
        background-color: #38BDF8;
        color: #0F172A;
        border: none;
        padding: 12px 24px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        font-weight: bold;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 8px;
        transition-duration: 0.2s;
        box-shadow: 0 4px 6px -1px rgba(56, 189, 248, 0.2);
    " onmouseover="this.style.backgroundColor='#0EA5E9'" onmouseout="this.style.backgroundColor='#38BDF8'">
        📄 Generate & Download PDF Report
    </button>
    """
    st.components.v1.html(print_button_html, height=60)

            # Pure Car Mathematical Formulas
            car_loan_principal = car_price - car_down_p
            car_months = car_tenure * 12
            car_monthly_rate = (car_rate / 12) / 100
            if car_monthly_rate > 0:
                car_emi = (car_loan_principal * car_monthly_rate * (1 + car_monthly_rate) ** car_months) / (
                        (1 + car_monthly_rate) ** car_months - 1)
            else:
                car_emi = car_loan_principal / car_months

            car_total_payout = car_emi * car_months
            car_total_interest = car_total_payout - car_loan_principal
            car_burden_ratio = (car_total_interest / car_price) * 100

        st.markdown("""
        <div style="
            position: relative; 
            background-image: linear-gradient(to right, rgba(15, 23, 42, 0.95) 40%, rgba(15, 23, 42, 0.3)), 
                              url('https://images.unsplash.com/photo-1747324660326-0864079a32e8?q=80&w=1161&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'); 
            background-size: cover; background-position: 50% 75%; padding: 35px 40px; border-radius: 16px; margin-bottom: 25px; border: 1px solid #334155;
        ">
            <span style="background-color: #38BDF822; color: #38BDF8; padding: 4px 12px; border-radius: 20px; font-size: 11px; font-weight: 700; letter-spacing: 1.5px; text-transform: uppercase; border: 1px solid #38BDF844;">
                Four-Wheeler Terminal Active
            </span>
            <h1 style="margin: 10px 0 4px 0; font-family: 'Plus Jakarta Sans', sans-serif; font-size: 32px; font-weight: 800; color: #F8FAFC; letter-spacing: -0.5px;">
                AUTO INTELLIGENCE
            </h1>
            <p style="margin: 0; color: #94A3B8; font-family: 'Inter', sans-serif; font-size: 14px;">
                Deconstruct vehicle depreciation, hidden taxes, and high-capital interest margins.
            </p>
        </div>
        """, unsafe_allow_html=True)

        tab_car_basic, tab_car_operating, tab_car_optimal = st.tabs(["📊 Basic Loan Breakdown", "📉Operating Cost","⚡ Optimal Finance Plan"])

        with tab_car_basic:
            col_outputs_car_d, col_outputs_car_i = st.columns([1, 1.2], gap="large")

            with col_outputs_car_d:

                # 1. Standard Slate Card with Cyber Sky Blue Text
                card_car_emi = create_kpi_card(
                    title="Estimated Monthly Payout (EMI)",
                    value=f"₹{int(car_emi):,}",
                    text_color="#38BDF8"
                )

                # 2. Special Green Highlight Card with Custom Gradient Background
                card_car_total = create_kpi_card(
                    title="Total Effective Loan",
                    value=f"₹{int(car_total_payout):,}",
                    text_color="#F8FAFC",
                    bg_style="background-color: #1E293B; border: 1px solid #22C55E44; background-image: linear-gradient(to right, #1E293B, #14532D22);"
                )

                # 3. Standard Slate Card with Silver White Text
                card_car_interest = create_kpi_card(
                    title="Total Interest Amount",
                    value=f"₹{int(car_total_interest):,}",
                    text_color="#F8FAFC"
                )

                # 4. The Financial Friction / Burden Ratio Card
                card_car_burden = create_kpi_card(
                    title="Total Outflow Interest Leakage",
                    value=f"{car_burden_ratio:.1f}%",
                    text_color="#F43F5E"  # High-end Coral Warning Red
                )

                # Render all four cards to the screen cleanly
                st.markdown(card_car_emi + card_car_total + card_car_interest + card_car_burden, unsafe_allow_html=True)

            with col_outputs_car_i:
                with st.container(border=True):
                    chart_view_car = st.radio(
                        "Select Visualization Horizon",
                        options=["Total Lifetime", "Yearly Breakdown"],
                        horizontal=True,
                        key="view_car",
                        label_visibility="collapsed"
                    )
                    # Generate list of years dynamically based on user's input tenure
                    car_year_options = [f"Year {i}" for i in range(1, int(car_tenure) + 1)]

                    # CASE A: TOTAL LIFETIME COST RING
                    if chart_view_car == "Total Lifetime":
                        car_labels = ['Principal Loan Amount', 'Total Interest Cost']
                        car_values = [int(car_loan_principal), int(car_total_interest)]
                        selected_car_year_str = st.selectbox("Select Target Year Analysis", options="NA",
                                                             key="sb_car_yr")
                        chart_title = "Lifetime Cost Matrix"

                    # CASE B: YEARLY DRILLDOWN CHARTS
                    else:
                        selected_car_year_str = st.selectbox("Select Target Year Analysis", options=car_year_options,
                                                             key="sb_car_yr")
                        selected_car_year = int(selected_car_year_str.split()[-1])

                        # Math to calculate specific year's interest and principal using amortization loop
                        car_remaining_balance = car_loan_principal
                        car_year_interest = 0
                        car_year_principal = 0

                        # Calculate amortization scheduling month by month up to target year
                        for m in range(1, int(car_months) + 1):
                            car_current_month_interest = car_remaining_balance * car_monthly_rate
                            car_current_month_principal = car_emi - car_current_month_interest
                            car_remaining_balance -= car_current_month_principal

                            # If this month falls inside our target year, log it!
                            if ((m - 1) // 12) + 1 == selected_car_year:
                                car_year_interest += car_current_month_interest
                                car_year_principal += car_current_month_principal

                        car_labels = [f'{selected_car_year_str} Principal Paid', f'{selected_car_year_str} Interest Cost']
                        car_values = [int(car_year_principal), int(car_year_interest)]
                        chart_title = f"{selected_car_year_str} Repayment Breakdown"

                    # Render the dynamic Plotly ring based on selected logic state
                    fig_car = px.pie(
                        names=car_labels,
                        values=car_values,
                        hole=0.6,
                        color_discrete_sequence=['#15803D', '#B91C1C']
                    )

                    fig_car.update_layout(
                        title=dict(text=chart_title, x=0.5, y=0.95, font=dict(size=14, weight='bold', color='#94A3B8')),
                        margin=dict(t=50, b=20, l=10, r=10),
                        showlegend=True,
                        legend=dict(orientation="h", yanchor="bottom", y=-0.1, xanchor="center", x=0.5),
                        paper_bgcolor="rgba(0,0,0,0)",
                        plot_bgcolor="rgba(0,0,0,0)",
                        font=dict(family="Inter, sans-serif", color="#F8FAFC", size=13)
                    )

                    fig_car.update_traces(
                        hovertemplate="<b>%{label}</b><br>Amount: ₹%{value:,}<br>Percentage: %{percent}<extra></extra>",
                        textinfo='percent',
                        textfont=dict(size=14, weight='bold', color='#FFFFFF')
                    )

                    st.plotly_chart(fig_car, use_container_width=True, config={'displayModeBar': False})

        with tab_car_operating:
            st.write("")  # Clear structural spacer

            # Segmented structural picker at the top
            car_propulsion_type = st.radio(
                "Select Vehicle Engine Variant",
                options=["Fuel (Petrol/Diesel)", "Electric (EV)"],
                horizontal=True,
                key="c_propulsion_toggle",
                label_visibility="collapsed"
            )
            st.write("")

            # ----------------------------------------------------
            # CONDITION A: FUEL (PETROL) CALCULATION BLOCK
            # ----------------------------------------------------
            if car_propulsion_type == "Fuel (Petrol/Diesel)":
                col_op_inputs_l, col_op_inputs_r = st.columns(2, gap="medium")

                with col_op_inputs_l:
                    st.markdown("##### 🌆 City Commute Split")
                    c_weekly_city_km = st.number_input("Weekly City Distance (km)", min_value=0, max_value=2000,
                                                       value=150,
                                                       step=5, key="c_fuel_cc_km")
                    c_city_mileage = st.number_input("City Mileage (km/L)", min_value=1, max_value=90, value=12,
                                                     step=1, key="c_fuel_cc_mlg")

                with col_op_inputs_r:
                    st.markdown("##### 🛣️ Highway Commute Split")
                    c_weekly_hwy_km = st.number_input("Weekly Highway Distance (km)", min_value=0, max_value=1500,
                                                      value=100, step=20, key="c_fuel_hw_km")
                    c_hwy_mileage = st.number_input("Highway Mileage (km/L)", min_value=1, max_value=95, value=17,
                                                    step=1, key="c_fuel_hw_mlg")
                st.markdown("##### 🛠️ Fixed Maintenance Overhead")
                col1, col2, col3 = st.columns(3)
                with col1:
                    c_fuel_price = st.number_input("Local Petrol/Diesel Price (₹/L)", min_value=60.0, max_value=1000.0,
                                                   value=104.5, step=0.5, key="c_fuel_price_val")
                with col2:
                    c_annual_service = st.number_input("Annual Servicing Costs (₹)", min_value=100, max_value=100000,
                                                       value=20000, step=500, key="c_fuel_srv")
                with col3:
                    c_annual_od_ins = st.number_input("Annual Own Damage Insurance Renewal (₹)", min_value=100,
                                                      max_value=100000, value=28000, step=500, key="c_fuel_ins")

                # Petrol Processing Engine Math
                c_monthly_city_dist = c_weekly_city_km * 4.33
                c_monthly_hwy_dist = c_weekly_hwy_km * 4.33
                c_total_monthly_dist = c_monthly_city_dist + c_monthly_hwy_dist

                c_fuel_city_liters = c_monthly_city_dist / c_city_mileage if c_city_mileage > 0 else 0
                c_fuel_hwy_liters = c_monthly_hwy_dist / c_hwy_mileage if c_hwy_mileage > 0 else 0
                c_total_fuel_liters = c_fuel_city_liters + c_fuel_hwy_liters

                c_true_efficiency = c_total_monthly_dist / c_total_fuel_liters if c_total_fuel_liters > 0 else 0
                c_monthly_running_cost = c_total_fuel_liters * c_fuel_price
                c_monthly_fixed_overhead = (c_annual_service + c_annual_od_ins) / 12

                efficiency_display_str = f"{c_true_efficiency:.1f} km/L"
                sub_caption_str = f"Total Fuel Burned: {c_total_fuel_liters:.1f} Liters/mo"

            # ----------------------------------------------------
            # CONDITION B: ELECTRIC (EV) CALCULATION BLOCK
            # ----------------------------------------------------
            else:
                col_op_inputs_l, col_op_inputs_r = st.columns(2, gap="medium")

                with col_op_inputs_l:
                    st.markdown("##### 🌆 City Electric Split")
                    c_weekly_city_km = st.number_input("Daily City Distance (km)", min_value=0, max_value=200,
                                                       value=150,
                                                       step=5, key="c_ev_cc_km")
                    c_city_efficiency = st.number_input("City Range Efficiency (km/kWh)", min_value=1, max_value=120,
                                                        value=7, step=1, key="c_ev_cc_eff")

                with col_op_inputs_r:
                    st.markdown("##### 🛣️ Highway Electric Split")
                    c_weekly_hwy_km = st.number_input("Weekly Highway Distance (km)", min_value=0, max_value=1500,
                                                      value=100, step=20, key="c_ev_hw_km")
                    c_hwy_efficiency = st.number_input("Highway Range Efficiency (km/kWh)", min_value=1, max_value=120,
                                                       value=5, step=1, key="c_ev_hw_eff")
                st.markdown("##### 🛠️ EV Maintenance Overhead")

                col1, col2, col3 = st.columns(3)
                with col1:
                    c_elec_rate = st.number_input("Electricity Cost (₹/Unit per kWh)", min_value=1.0, max_value=100.0,
                                                  value=10.5, step=0.5, key="c_ev_elec_rate")
                with col2:
                    c_annual_service = st.number_input("Annual EV Inspection/Brakes (₹)", min_value=200,
                                                       max_value=200000, value=5000, step=200, key="c_ev_srv")
                with col3:
                    c_annual_od_ins = st.number_input("Annual Insurance Renewal (₹)", min_value=200,
                                                      max_value=120000, value=35000, step=500, key="c_ev_ins")

                # EV Processing Engine Math
                c_monthly_city_dist = c_weekly_city_km * 4.33
                c_monthly_hwy_dist = c_weekly_hwy_km * 4.33
                c_total_monthly_dist = c_monthly_city_dist + c_monthly_hwy_dist

                c_energy_city_kwh = c_monthly_city_dist / c_city_efficiency if c_city_efficiency > 0 else 0
                c_energy_hwy_kwh = c_monthly_hwy_dist / c_hwy_efficiency if c_hwy_efficiency > 0 else 0
                c_net_energy_stored = c_energy_city_kwh + c_energy_hwy_kwh

                # Incorporating standard 10% structural loss factor on charger wall pull
                c_total_billed_units = c_net_energy_stored * 1.10

                c_true_efficiency = c_total_monthly_dist / c_total_billed_units if c_total_billed_units > 0 else 0
                c_monthly_running_cost = c_total_billed_units * c_elec_rate
                c_monthly_fixed_overhead = (c_annual_service + c_annual_od_ins) / 12

                efficiency_display_str = f"{c_true_efficiency:.1f} km/kWh"
                sub_caption_str = f"Meter Load: {c_total_billed_units:.1f} Units (incl. 10% loss)"

            # ----------------------------------------------------
            # UNIFIED METRIC RENDER PIPELINE
            # ----------------------------------------------------
            c_total_monthly_operating = c_monthly_running_cost + c_monthly_fixed_overhead
            c_total_monthly_outflow = c_total_monthly_operating + car_emi

            st.markdown("---")
            st.markdown("### 📊 Operational Cost Matrix")

            col_op_m1, col_op_m2, col_op_m3, col_op_m4 = st.columns(4)

            with col_op_m1:
                card_running_ops = create_kpi_card(
                    title="Monthly Running Outflow",
                    value=f"₹{int(c_monthly_running_cost):,}",
                    text_color="#38BDF8"
                )
                st.markdown(card_running_ops, unsafe_allow_html=True)
                st.caption(f"Monthly Travel Range: {int(c_total_monthly_dist):,} km")

            with col_op_m2:
                card_efficiency_ops = create_kpi_card(
                    title="True Blended Efficiency",
                    value=efficiency_display_str,
                    text_color="#F8FAFC"
                )
                st.markdown(card_efficiency_ops, unsafe_allow_html=True)
                st.caption(sub_caption_str)

            with col_op_m3:
                card_total_ops = create_kpi_card(
                    title="Total Operating Burden",
                    value=f"₹{int(c_total_monthly_operating):,}",
                    text_color="#38BDF8",
                    bg_style="background-color: #1E293B; border: 1px solid #38BDF844; background-image: linear-gradient(to right, #1E293B, #0369A111);"
                )
                st.markdown(card_total_ops, unsafe_allow_html=True)
                st.caption(f"Fixed Maintenance Base: ₹{int(c_monthly_fixed_overhead):,}/mo")

            with col_op_m4:
                card_total_out = create_kpi_card(
                    title="Total Monthly Outflow",
                    value=f"₹{int(c_total_monthly_outflow):,}",
                    text_color="#38BDF8",
                    bg_style="background-color: #1E293B; border: 1px solid #38BDF844; background-image: linear-gradient(to right, #1E293B, #0369A111);"
                )
                st.markdown(card_total_out, unsafe_allow_html=True)
                st.caption(f"Includes Loan EMI: ₹{int(car_emi):,}/mo")

        with tab_car_optimal:

            col_savings, col_equal, col_burden, col_plus, col_emi = st.columns([5, 1, 5, 1, 3.5])

            with col_savings:
                st.write("")
                c_m_savings = st.number_input(
                    label="Monthly Comfortable Savings",
                    value=int(c_total_monthly_outflow),  # Scaled default for car planning
                    step=1000,
                    label_visibility="visible",
                    key="c_opt_m_savings",
                    help = "Ideally less than 10% of user's Monthly Net Income, can be stretched to 15%. More than 15% is financially Risky."
                )

            # Column 2: The Equal Sign
            with col_equal:
                render_operator("=")

            # Column 3: Total Operating Burden Card
            with col_burden:
                st.markdown(
                    create_kpi_card(
                        title="Total Monthly Operating Cost",
                        value=f"₹{int(c_total_monthly_operating):,}"
                    ),
                    unsafe_allow_html=True
                )

            # Column 4: The Plus Sign
            with col_plus:
                render_operator("+")

            cmx_emi = c_m_savings - c_total_monthly_operating

            # Column 5: Max Allowable EMI Card
            with col_emi:
                st.markdown(
                    create_kpi_card(
                        title="Max Allowable EMI",
                        value=f"₹{int(cmx_emi):,}"
                    ),
                    unsafe_allow_html=True
                )

            # Dropdown Explanation Section placed right below the metric rows
            with st.expander("💡 The Financial Beta Test Strategy (Logic Behind This Equation)"):
                st.markdown(f"""
                                ### 🧪 The Sandbox Ownership Simulation
                                This matrix doesn't just calculate affordability—it **stress-tests your behavior** before you sign a legally binding bank contract.

                                ---

                                ### 🎯 Why This Strategy is Bulletproof:

                                * **🛡️ Zero Lifestyle Shock**
                                  You adjust to the financial strain *before* the vehicle arrives. 
                                  * **Before Purchase:** **₹{int(c_m_savings):,}/mo** flows entirely into your **Savings Pool**.
                                  * **After Purchase:** That exact same **₹{int(c_m_savings):,}/mo** splits into **₹{int(c_total_monthly_operating):,}** (Fuel/Service) + **₹{int(cmx_emi):,}** (Bank EMI). 
                                  * *Net lifestyle impact:* **Identical.** Only the direction of the cash flow changes.

                                * **🛑 Safe Sabotage Buffer**
                                  If a life emergency hits in Month 3 and breaks your budget, **nothing bad happens**. No missed bank EMIs, no ruined credit score, no repossession trucks. You simply reset the simulation.

                                * **⚙️ Self-Correcting Down Payment Engine**
                                  If the bike's price tag breaches your current budget, you don't give up. You just run the beta test longer. The capital stacking up in your sandbox account naturally inflates your **Down Payment**, crushing the future loan principal down until it fits your rule perfectly.

                                ---

                                > **⚠️ The Ultimate Rule:** If you cannot comfortably survive the mock outflow of **₹{int(c_m_savings):,}/mo** during this simulation phase, your life isn't ready for the vehicle yet. Let the simulation protect your wealth.
                                """)


            st.markdown("### ⚡ Short-Term Purchase Runway", help = "Vehicle prices may increase over time due to inflation and market conditions."
                                                                   " This calculator does not predict future on-road price inflation "
                                                                   "because long-term pricing is highly unpredictable.\n\n"
                                                                   " The projection assumes your short-term vehicle savings are parked in instruments such as:\n"
                                                                   " 1) High-return mutual funds\n"
                                                                   " 2) Liquid/arbitrage funds\n"
                                                                   " 3) Recurring deposits (RDs).\n\n"
                                                                   "Historically, these often generate returns that partially or fully "
                                                                   "offset average vehicle inflation over shorter ownership timelines.")

            # 1. User Choice for Aggressive Short Tenure Horizon
            c_test_tenure = st.selectbox(
                "Select Beta Test Tenure Strategy",
                options=[1, 1.5, 2, 2.5, 3, 3.5, 4],
                format_func=lambda x: f"{x} Year Plan ({int(x * 12)} Months)",
                key="c_beta_tenure_pick"
            )

            # 2. Mathematical Calculations Pipeline
            c_test_months = c_test_tenure * 12

            # Deriving the monthly interest rate from your main car sidebar lever (car_rate)
            c_test_monthly_rate = (car_rate / 12) / 100

            # Reverse compounding engine: Calculate actual max loan principal capacity
            if c_test_monthly_rate > 0:
                c_max_principal_loan = cmx_emi * (
                        ((1 + c_test_monthly_rate) ** c_test_months - 1) /
                        (c_test_monthly_rate * (1 + c_test_monthly_rate) ** c_test_months)
                )
            else:
                c_max_principal_loan = cmx_emi * c_test_months

            c_total_loan_capacity = cmx_emi * c_test_months

            # 20% Asset Valuation Boundary Floor
            c_cash_floor_limit = car_price * 0.20

            # ----------------------------------------------------
            # SCENARIO A: FINANCING IS TRIVIAL -> GO FOR FULL DOWN
            # ----------------------------------------------------
            if c_total_loan_capacity < c_cash_floor_limit or c_max_principal_loan < 100000:
                st.success("### 🎉 Strategy Recommendation: GO FOR FULL DOWN PAYMENT")

                # Calculate timeline to buy it outright with 100% cash
                c_months_to_full_cash = car_price / c_m_savings if c_m_savings > 0 else 0

                rejection_reason = ""
                if c_max_principal_loan < 30000:
                    rejection_reason = f"Your maximum borrowable principal (**₹{int(c_max_principal_loan):,}**) falls below the real-world banking threshold of **₹100,000**. No major lender will approve a vehicle loan this low."
                else:
                    rejection_reason = f"Your true borrowable principal capacity (**₹{int(c_max_principal_loan):,}**) falls beneath 20% of the vehicle's sticker value (**₹{int(c_cash_floor_limit):,}**). Taking a loan for this small an amount is an inefficient capital drain."

                st.markdown(f"""
                        {rejection_reason}

                        * **Strategic Direction:** Avoid all banking friction, hidden processing fees, and interest leakage.
                        * **Beta Test Target:** Accumulate 100% cash to buy the asset outright.
                        * **Time to Destination:** Approximately **{c_months_to_full_cash:.1f} months** of running your current savings rate of **₹{int(c_m_savings):,}/mo**.
                        """)

            # ----------------------------------------------------
            # SCENARIO B: CALCULATE MINIMUM DOWN PAYMENT & TIMELINE
            # ----------------------------------------------------
            else:
                st.warning("### 📈 Strategy Recommendation: STRUCTURED DOWN PAYMENT PLAN")

                c_months_to_full_cash = car_price / c_m_savings
                if c_max_principal_loan >= car_price:
                    c_min_down_payment = 0.0
                    c_time_to_down_payment = 0.0
                    c_actual_loan_needed = car_price
                else:
                    c_min_down_payment = car_price - c_max_principal_loan
                    c_time_to_down_payment = c_min_down_payment / c_m_savings if c_m_savings > 0 else 0
                    c_actual_loan_needed = c_max_principal_loan

                # Render Layout Split
                c_col_d1, c_col_d2, c_col_d3 = st.columns(3)

                with c_col_d1:
                    card_min_dp = create_kpi_card(
                        title="Required Target Down Payment",
                        value=f"₹{int(c_min_down_payment):,}",
                        text_color="#3B6896" if c_min_down_payment > 0 else "#22C55E"
                    )
                    st.markdown(card_min_dp, unsafe_allow_html=True)
                    st.caption(f"Bridges the gap for an actual principal loan of ₹{int(c_actual_loan_needed):,}.")

                with c_col_d2:
                    card_time_dp = create_kpi_card(
                        title="Beta Test Phase Duration",
                        value=f"{c_time_to_down_payment:.1f} Months",
                        text_color="#22C55E"
                    )
                    st.markdown(card_time_dp, unsafe_allow_html=True)
                    st.caption(f"Months required at a save rate of ₹{int(c_m_savings):,}/mo.")
                with c_col_d3:
                    total_interest_dp = create_kpi_card(
                        title="Total Interest Paid",
                        value=f"₹{int(c_total_loan_capacity - c_max_principal_loan):,}",
                        text_color="#F43F5E"
                    )
                    st.markdown(total_interest_dp, unsafe_allow_html=True)
                    st.caption(
                        f"Extra {int(((c_total_loan_capacity - c_max_principal_loan) / car_price) * 100):,}% than actual Initial on Road Price.")

                st.markdown(f"""
                    ### 🎯 Beta Test Action Plan

                    * **🛠️ The Sandbox Routine:** Lock down and divert **₹{int(c_m_savings):,}/mo** into your simulation pool.
                    * **⏳ Testing Timeline:** Run this drill for exactly **{c_time_to_down_payment:.1f} Months**.
                    * **💰 Target Down Payment:** Once your pool hits **₹{int(c_min_down_payment):,}**, sign the paperwork. Your daily lifestyle won't shift a single millimeter.

                    ---

                    ### ⚡ The Time-vs-Money Trade-Off:
                    * **🚀 Time Saved:** You hit the road **{(c_months_to_full_cash - c_time_to_down_payment):.1f} Months earlier** than waiting to buy the vehicle with 100% full cash down.
                    * **🏆 Asset Ownership:** You will 100% own the vehicle **{(car_months - c_time_to_down_payment - c_test_months):.1f} Months** before the initial **{int(car_tenure):,} Years** loan.
                    * **💸 Premium Paid:** The total interest cost for skipping time is just **₹{int(c_total_loan_capacity - c_max_principal_loan):,}** extra.
                    """)
