import hashlib
import secrets

class Ballot:
    """
    A ballot that exists in a specific, secret manner
    """
    def __init__(self, ballot_number: str, chosen_candidate_id: str, voter_comments: str):
        self.ballot_number = ballot_number
        self.chosen_candidate_id = chosen_candidate_id
        self.voter_comments = voter_comments


def generate_ballot_number(voter_id: str) -> str:
    """
    Produces a ballot number.

    :param voter_id: A unique identifier for the voter.
    :return: A string representing a ballot number that satisfies the conditions.
    """
     
    # TODO: Implement this! Feel free to add parameters to this method, if necessary
    # Use a cryptographic hash function (SHA-256) to hash the voter_id and add some randomness
    # This ensures uniqueness, irreversibility, and adds randomness to minimize fraud risk
    ballot_number = hashlib.sha256((voter_id + secrets.token_hex(16)).encode()).hexdigest()
    return ballot_number

  # Example usage:
  # voter_id = "12345"  # Replace with the actual unique identifier for the voter
  # ballot_number = generate_ballot_number(voter_id)
   # print(ballot_number)

   #raise NotImplementedError()
