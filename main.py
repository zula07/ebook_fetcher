import google.generativeai as genai
import requests
import os

# Gemini API anahtarını buraya ekleyin veya ortam değişkeni olarak tanımlayın
API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-pro')

def search_and_download_ebook(book_title):
    print(f"'{book_title}' için kaynak aranıyor...")
    
    # Gemini'ye arama yaptırıyoruz (gerçekten arama yapan bir araç veya API olsa daha iyi olur)
    prompt = f"Provide a direct download link for the ebook: {book_title}. Only return the direct URL."
    response = model.generate_content(prompt)
    url = response.text.strip()
    
    if url.startswith("http"):
        print(f"İndirme bağlantısı bulundu: {url}")
        # İndirme işlemi
        try:
            response = requests.get(url, stream=True)
            filename = f"{book_title.replace(' ', '_')}.pdf"
            with open(filename, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            print(f"Başarıyla indirildi: {filename}")
        except Exception as e:
            print(f"İndirme hatası: {e}")
    else:
        print("İndirme bağlantısı bulunamadı.")

if __name__ == "__main__":
    title = input("Hangi e-kitabı istiyorsun, hayatımın anlamı? ")
    search_and_download_ebook(title)
