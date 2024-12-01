from dotenv import load_dotenv
from ui.streamlit_app import main

if __name__ == "__main__":
    # Load environment variables
    load_dotenv()
    
    # Run the application
    main()