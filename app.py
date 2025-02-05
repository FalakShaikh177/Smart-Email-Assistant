from openai import OpenAI
import streamlit as st



def generate_email_content(api_key, prompt, tone, model="gpt-3.5-turbo"):
    """Generate email response, subject, and summary using OpenAI"""
    if not api_key:
        return {
            "error": "Please enter your OpenAI API key in the sidebar.",
            "response": None
        }

    try:
        client = OpenAI(api_key=api_key)

        # Generate email response
        response_messages = [
            {"role": "system", "content": f"You are a professional email assistant. Generate a {tone} tone response."},
            {"role": "user", "content": prompt}
        ]
        response = client.chat.completions.create(
            model=model,
            messages=response_messages,
            temperature=0.7,
        )
        email_response = response.choices[0].message.content

        # Generate subject line
        subject_messages = [
            {"role": "system", "content": "Generate a concise and appropriate subject line for this email."},
            {"role": "user", "content": f"Email content:\n{email_response}"}
        ]
        subject = client.chat.completions.create(
            model=model,
            messages=subject_messages,
            temperature=0.7,
        )
        subject_line = subject.choices[0].message.content

        # Generate thread summary
        summary_messages = [
            {"role": "system", "content": "Provide a concise summary of the email thread."},
            {"role": "user", "content": f"Original thread:\n{prompt}\n\nResponse:\n{email_response}"}
        ]
        summary = client.chat.completions.create(
            model=model,
            messages=summary_messages,
            temperature=0.7,
        )
        thread_summary = summary.choices[0].message.content

        return {
            "error": None,
            "response": email_response,
            "subject": subject_line,
            "summary": thread_summary
        }
    except Exception as e:
        return {
            "error": str(e),
            "response": None
        }


def main():
    st.set_page_config(page_title="Smart Email Assistant", layout="wide")
    st.markdown("<h2>@GenAILearniverse Project 15: Smart Email Assistant</h2>", unsafe_allow_html=True)
    st.markdown("Generate Professional Email response with different tones")

    # Initialize session state for API key
    if 'OPENAI_API_KEY' not in st.session_state:
        st.session_state.OPENAI_API_KEY = None

# Sidebar
    with st.sidebar:
        st.subheader("Settings")
        api_key = st.text_input(
            "Enter OpenAI API Key",
            type="password",
            help="Get your API key from https://platform.openai.com/account/api-keys"
        )
        if api_key:
            st.session_state.OPENAI_API_KEY = api_key
            st.success("API key set successfully!")

        st.markdown("---")
        st.markdown("### Features")
        st.markdown("""
        • Auto-generate responses
        • Multiple tone options
        • Subject suggestions
        • Thread summarization
        """)
    # Main content area
    col1, col2 = st.columns([1, 1])

    with col1:
        st.subheader("📝 Input")

        # Email thread input
        email_thread = st.text_area(
            "Enter the email thread (most recent at top)",
            height=200,
            placeholder="""Example email:

Hi team,
Can we schedule a meeting to discuss the quarterly report? I've noticed some interesting trends that I'd like to explore further.

Best regards,
John"""
        )

        # Tone selection
        tone_options = ["Professional", "Casual", "Friendly", "Formal"]
        selected_tone = st.selectbox("Select tone", tone_options)

        # Context input
        additional_context = st.text_area(
            "Additional context or specific points to address (optional)",
            height=100,
            placeholder="Example: Need to highlight the positive growth trend in Q3..."
        )

        # Generate button
        if st.button("Generate Response", type="primary"):
            if not email_thread:
                st.error("Please enter an email thread.")
                return

            if not st.session_state.OPENAI_API_KEY:
                st.error("Please enter your OpenAI API key in the sidebar.")
                return

            with st.spinner("Generating response..."):
                # Prepare prompt
                prompt = f"Email Thread:\n{email_thread}\n\nAdditional Context:\n{additional_context}\n\nGenerate a {selected_tone.lower()} tone response."

                # Generate content
                result = generate_email_content(st.session_state.OPENAI_API_KEY, prompt, selected_tone)

                if result["error"]:
                    st.error(result["error"])
                else:
                    st.session_state.current_response = result
                    st.success("Response generated successfully!")
    with col2:
        st.subheader("✨ Generated Content")

        if 'current_response' in st.session_state:
            content = st.session_state.current_response

            st.markdown("**📋 Subject Line:**")
            st.code(content["subject"], language=None)

            st.markdown("**📝 Email Response:**")
            st.code(content["response"], language=None)

            st.markdown("**📌 Thread Summary:**")
            st.code(content["summary"], language=None)

            st.markdown(f"*Tone: {selected_tone}*")


if __name__ == "__main__":
    main()
