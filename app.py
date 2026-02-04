import streamlit as st

# ===============================
# 页面基础设置
# ===============================
st.set_page_config(layout="wide")

# ===============================
# 初始化状态
# ===============================
if "show_settings" not in st.session_state:
    st.session_state.show_settings = False

if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False

# ===============================
# 全局 CSS（根据模式切换）
# ===============================
if st.session_state.dark_mode:
    st.markdown(
        """
        <style>
        /* ===============================
           全局背景
        =============================== */
        html, body, [data-testid="stApp"] {
            background-color: #0d1117;
            color: #e6edf3;
        }

        /* ===============================
           Sidebar 背景
        =============================== */
        [data-testid="stSidebar"] {
            background-color: #0b0f14 !important;
            border-right: 1px solid #1f2933;
        }

        /* Sidebar 内文字 */
        [data-testid="stSidebar"] * {
            color: #c9d1d9 !important;
        }

        /* ===============================
           Selectbox / Input / Textarea
        =============================== */
        div[data-baseweb="select"] > div {
            background-color: #161b22 !important;
            border: 1px solid #30363d !important;
            color: #e6edf3 !important;
        }

        div[data-baseweb="select"] span {
            color: #e6edf3 !important;
        }

        input, textarea {
            background-color: #161b22 !important;
            color: #e6edf3 !important;
            border: 1px solid #30363d !important;
        }

        /* 下拉箭头 */
        svg {
            fill: #8b949e !important;
        }

        /* ===============================
           Button（解决白色按钮）
        =============================== */
        button {
            background-color: #1f2933 !important;
            color: #e6edf3 !important;
            border: 1px solid #2d333b !important;
            box-shadow: none !important;
        }

        button:hover {
            background-color: #2a2f3a !important;
            border-color: #3b4252 !important;
        }

        /* ===============================
           Radio / Checkbox
        =============================== */
        label {
            color: #c9d1d9 !important;
        }

        /* ===============================
           设置浮窗
        =============================== */
        .settings-modal {
            background-color: #161b22;
            border: 1px solid #30363d;
            color: #e6edf3;
        }

        </style>
        """,
        unsafe_allow_html=True
    )

else:
    st.markdown(
        """
        <style>
        .settings-modal {
            background: white;
            color: black;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# ===============================
# 设置弹窗 CSS（通用）
# ===============================
st.markdown(
    """
    <style>
    .settings-modal {
        position: fixed;
        right: 32px;
        bottom: 32px;
        width: 320px;
        border-radius: 12px;
        box-shadow: 0 10px 28px rgba(0,0,0,0.25);
        padding: 16px;
        z-index: 9999;
    }

    .settings-divider {
        margin: 8px 0;
        border-top: 1px solid #444;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ===============================
# 左侧栏
# ===============================
st.sidebar.title("📁 项目管理")
st.sidebar.markdown("---")

current_project = st.sidebar.radio(
    "历史项目",
    ["中医证候分析项目", "慢性疲劳研究", "实验记录"]
)

st.sidebar.button("➕ 新建项目")

st.sidebar.markdown("<br><br><br>", unsafe_allow_html=True)
st.sidebar.markdown("---")

col_info, col_setting = st.sidebar.columns(2)

with col_info:
    st.button("❓")

with col_setting:
    if st.button("⚙️"):
        st.session_state.show_settings = not st.session_state.show_settings
        st.rerun()

# ===============================
# 设置浮窗
# ===============================
if st.session_state.show_settings:
    st.markdown(
        """
        <div class="settings-modal">
            <h4>⚙️ 系统设置</h4>
            <div class="settings-divider"></div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.selectbox(
        "模型策略",
        ["默认", "稳定", "实验"],
        key="setting_model_mode"
    )

    if st.button(
        "🌞 切换为日间模式" if st.session_state.dark_mode else "🌙 切换为黑暗模式"
    ):
        st.session_state.dark_mode = not st.session_state.dark_mode
        st.rerun()

    st.checkbox("开启调试模式", key="setting_debug")

# ===============================
# 主界面顶部
# ===============================
col1, col2 = st.columns([4, 1])
with col2:
    current_model = st.selectbox("当前模型", ["Qwen", "ChatGPT", "DeepSeek"])

st.markdown("---")

# ===============================
# 主内容
# ===============================
st.title(current_project)
st.caption("基于中医证候与经典文献的智能辅助分析")

st.info(
    f"""
    本系统基于 **检索增强生成（RAG）技术**  
    当前使用模型：**{current_model}**

    ⚠️ 本系统仅用于教学与科研辅助，不构成医疗建议
    """
)

st.subheader("症状输入")

symptom_text = st.text_area(
    "请输入患者症状描述：",
    placeholder="例如：不耐疲劳，口燥、咽干，心烦失眠……",
    height=150
)

if st.button("开始智能分析"):
    st.subheader("AI 诊疗分析结果")
    st.success(symptom_text if symptom_text else "（暂无症状输入）")
