import os
import shutil
from backend.drive_loader import download_documents
from backend.local_loader import load_local_documents
from backend.text_extractor import extract_text
from backend.vectorstore_builder import create_vectorstore
from backend.qa_chain import create_qa_chain, answer_question
import gradio as gr

DRIVE = "Drive"
LOCAL = "Local"

def analyseer_en_start(mode, folder_input, vraag):
    # Reset docs directory
    if os.path.exists("docs"):
        shutil.rmtree("docs")
    os.makedirs("docs", exist_ok=True)

    if mode == DRIVE:
        download_documents(folder_input)
    else:
        load_local_documents(folder_input)

    texts = []
    for root, dirs, files in os.walk("docs"):
        for fname in files:
            path = os.path.join(root, fname)
            t = extract_text(path)
            if t:
                texts.append(t)

    vs = create_vectorstore(texts)
    chain = create_qa_chain(vs)
    antwoord, bronnen = answer_question(chain, vraag)
    return f"{antwoord}\n\nBronnen:\n" + "\n".join(bronnen)

with gr.Blocks(title="AIDA3 Document AI Assistent") as demo:
    gr.Markdown("## AIDA3 - Kies Drive of Lokale Map")
    mode = gr.Radio([DRIVE, LOCAL], label="Laad van:", value=DRIVE)
    folder = gr.Textbox(label="Folder-ID (Drive) of lokaal pad", placeholder="Vul hier je Drive-folder-ID of lokale map in")
    vraag = gr.Textbox(label="Je vraag", placeholder="Stel hier je vraag over de documenten")
    output = gr.Textbox(label="Antwoord en bronnen", lines=10)
    btn = gr.Button("Analyseer")

    btn.click(fn=analyseer_en_start, inputs=[mode, folder, vraag], outputs=output)

if __name__ == "__main__":
    demo.launch()
