import csv
from collections import defaultdict

def combine_vote_counts(file1, file2, output_file="final_results.csv"):
    # Dictionary to store the combined vote counts
    vote_counts = defaultdict(int)

    # Helper function to read votes from a file
    def read_votes(file):
        with open(file, mode='r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Skip header row
            for row in reader:
                candidate = row[0]  # Candidate name and committee
                votes = int(row[1])  # Vote count
                vote_counts[candidate] += votes  # Add votes to the candidate

    # Read votes from both files
    read_votes(file1)
    read_votes(file2)

    # Sort candidates by vote count in descending order
    sorted_results = sorted(vote_counts.items(), key=lambda x: x[1], reverse=True)

    # Write the combined and sorted results to a new CSV file
    with open(output_file, mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Candidate", "Vote Count"])
        for candidate, votes in sorted_results:
            writer.writerow([candidate, votes])

    print(f"Final results saved to {output_file}")

# Example usage
combine_vote_counts("candidate_votes.csv", "candidate_votes(1).csv")
