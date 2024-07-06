import re
import csv
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def extract_movie_info(file_path, output_csv):
    logging.info(f"Starting to process file: {file_path}")
    
    movie_data = []
    current_movie = None
    current_link = None

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            
            # Check for movie name (starts with a number followed by a dot)
            match = re.match(r'^\d+\.\s(.+)$', line)
            if match:
                if current_movie and current_link:
                    movie_data.append((current_movie, current_link))
                    logging.info(f"Added movie: {current_movie}")
                current_movie = match.group(1)
                current_link = None
                logging.debug(f"Found new movie: {current_movie}")
            
            # Check for link
            elif line.startswith('<') and line.endswith('>'):
                link = line[1:-1]  # Remove < and >
                link = link.split('?')[0]  # Remove everything after ?
                if not current_link:
                    current_link = link
                    logging.debug(f"Found link for {current_movie}: {current_link}")

    # Add the last movie if exists
    if current_movie and current_link:
        movie_data.append((current_movie, current_link))
        logging.info(f"Added last movie: {current_movie}")

    logging.info(f"Finished processing. Total movies found: {len(movie_data)}")

    # Write to CSV
    logging.info(f"Writing data to CSV: {output_csv}")
    with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Movie Name', 'Movie Link'])  # Header
        writer.writerows(movie_data)

    logging.info("CSV file has been created successfully.")

# Usage
input_file = '2000 Movies.txt'
output_file = 'movie_data.csv'
extract_movie_info(input_file, output_file)