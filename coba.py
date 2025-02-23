import pandas as pd
import streamlit as st
from google_play_scraper import Sort, reviews
import time
from datetime import datetime, timedelta

# Main function
def main():
    st.title("Scraping Ulasan Aplikasi di Google Play Store")

    num_apps = st.number_input("Masukkan jumlah aplikasi yang ingin diambil ulasannya", min_value=1, value=1)

    app_ids = []
    app_names = []
    for i in range(num_apps):
        col1, col2 = st.columns(2)
        with col1:
            app_id = st.text_input(f"Masukkan ID aplikasi ke-{i+1} (contoh: com.gojek.gopay):")
        with col2:
            app_name = st.text_input(f"Masukkan nama aplikasi ke-{i+1}:")
        app_ids.append(app_id)
        app_names.append(app_name)

    max_reviews = st.number_input("Masukkan jumlah maksimum ulasan yang ingin diambil", min_value=1, value=1000)
    sleep_milliseconds = 3

    # Tambahkan input rentang waktu
    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input("Tanggal mulai", value=datetime.now() - timedelta(days=30))
    with col2:
        end_date = st.date_input("Tanggal akhir", value=datetime.now())

    if st.button("Mulai Pengambilan Ulasan"):
        reviews_data = []
        for app_id, app_name in zip(app_ids, app_names):
            st.write(f"Scraping reviews for app: {app_name}")
            result = []
            continuation_token = None

            progress_bar = st.progress(0)
            for i in range(0, max_reviews, 199):
                try:
                    new_result, continuation_token = reviews(
                        app_id,
                        continuation_token=continuation_token,
                        lang='id',
                        country='id',
                        sort=Sort.NEWEST,
                        filter_score_with=None,
                        count=min(max_reviews - len(result), 199)
                    )
                    if not new_result:
                        break
                    # Filter ulasan berdasarkan rentang tanggal dan tambahkan 'appName'
                    filtered_reviews = []
                    for review in new_result:
                        review_date = pd.to_datetime(review['at']).date()
                        if start_date <= review_date <= end_date:
                            filtered_reviews.append({
                                'content': review.get('content', ''),
                                'aplikasi': app_name,
                                'rating': review.get('score', None),  # Tambahkan rating
                                'at': review['at']
                            })
                    result.extend(filtered_reviews)
                    reviews_data.extend(filtered_reviews)
                    progress_bar.progress(min((i + len(new_result)) / max_reviews, 1.0))
                    if len(result) >= max_reviews:
                        break
                except Exception as e:
                    st.error(f"Error occurred: {e}")
                    time.sleep(5)

            if sleep_milliseconds:
                time.sleep(sleep_milliseconds / 1000)
                
        # Membuat DataFrame dari reviews_data
        df = pd.DataFrame(reviews_data)

        # Menampilkan DataFrame di Streamlit
        st.write(df)

        # Menyediakan opsi untuk mengunduh data
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Unduh data sebagai CSV",
            data=csv,
            file_name="reviews_data.csv",
            mime="text/csv",
        )

if __name__ == "__main__":
    main()
