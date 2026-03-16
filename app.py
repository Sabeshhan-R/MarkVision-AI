import streamlit as st
from nova_parser import parse_marksheet
from excel_export import export_excel

st.set_page_config(page_title="MarkVision AI", layout="wide")
st.title("🎯 MarkVision AI - Marksheet Extractor")
st.markdown("Upload scanned marksheet images and automatically extract data using Amazon Nova.")

files = st.file_uploader(
    "Upload marksheet images",
    type=["jpg", "png", "jpeg"],
    accept_multiple_files=True
)

if files:
    results = []
    
    with st.status("Processing images...", expanded=True) as status:
        for i, file in enumerate(files):
            st.write(f"Processing `{file.name}`...")
            image_bytes = file.read()
            
            # Determine media type for Nova
            media_type = "image/jpeg"
            if file.type == "image/png":
                media_type = "image/png"
            elif file.type in ["image/jpg", "image/jpeg"]:
                media_type = "image/jpeg"
            
            try:
                student = parse_marksheet(image_bytes, media_type=media_type)
                student["filename"] = file.name # Keep track of which file we're processing
                results.append(student)
            except Exception as e:
                st.error(f"Error processing {file.name}: {e}")
        
        status.update(label="Extraction complete!", state="complete", expanded=False)

    if results:
        st.subheader("Extracted Data Preview")
        st.table(results)

        excel_file = export_excel(results)
        
        st.success(f"Successfully processed {len(results)} files!")

        with open(excel_file, "rb") as f:
            st.download_button(
                label="📥 Download Excel Results",
                data=f,
                file_name="marksheet_results.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
else:
    st.info("Please upload one or more marksheet images to begin.")