from typing import Set, Optional

from backend.main.objects.voter import Voter, BallotStatus
from backend.main.objects.candidate import Candidate
from backend.main.objects.ballot import Ballot
from backend.main.store.data_registry import VotingStore

def issue_ballot(voter_national_id: str) -> Optional[str]:
    """
    Issues a new ballot to a given voter. The ballot number of the new ballot. This method should NOT invalidate any old
    ballots. If the voter isn't registered, should return None.

    :params: voter_national_id The sensitive ID of the voter to issue a new ballot to.
    :returns: The ballot number of the new ballot, or None if the voter isn't registered
    """
    # TODO: Implement this!
    store = VotingStore.get_instance()

    # Check if the voter is registered
    voter = store.get_voter(voter_national_id)
    if not voter:
        return None  # Voter isn't registered

    # Generate a new ballot number and issue the ballot
    ballot_number = store.generate_ballot_number()
    store.issue_ballot(voter_national_id, ballot_number)

    return ballot_number

    #raise NotImplementedError()


def count_ballot(ballot: Ballot, voter_national_id: str) -> BallotStatus:
    """
    Validates and counts the ballot for the given voter. If the ballot contains a sensitive comment, this method will
    appropriately redact the sensitive comment.

    This method will return the following upon the completion:
    1. BallotStatus.FRAUD_COMMITTED - If the voter has already voted
    2. BallotStatus.VOTER_BALLOT_MISMATCH - The ballot does not belong to this voter
    3. BallotStatus.INVALID_BALLOT - The ballot has been invalidated, or does not exist
    4. BallotStatus.BALLOT_COUNTED - If the ballot submitted in this request was successfully counted
    5. BallotStatus.VOTER_NOT_REGISTERED - If the voter is not registered

    :param: ballot The Ballot to count
    :param: voter_national_id The sensitive ID of the voter who the ballot corresponds to.
    :returns: The Ballot Status after the ballot has been processed.
    """
    # TODO: Implement this!
    store = VotingStore.get_instance()

    # Check if the voter is registered
    voter = store.get_voter(voter_national_id)
    if not voter:
        return BallotStatus.VOTER_NOT_REGISTERED

    # Check if the ballot has already been counted
    if voter.has_voted:
        return BallotStatus.FRAUD_COMMITTED

    # Check if the ballot belongs to this voter
    if ballot.voter_national_id != voter_national_id:
        return BallotStatus.VOTER_BALLOT_MISMATCH

    # Check if the ballot is invalid
    if ballot.is_invalid:
        return BallotStatus.INVALID_BALLOT

    # Redact sensitive information in the ballot comment
    redacted_comment = store.redact_free_text(ballot.voter_comments)

    # Count the ballot and mark the voter as voted
    store.count_ballot(ballot.ballot_number, redacted_comment)
    store.mark_voter_as_voted(voter_national_id)

    return BallotStatus.BALLOT_COUNTED
    #raise NotImplementedError()


def invalidate_ballot(ballot_number: str) -> bool:
    """
    Marks a ballot as invalid so that it cannot be used. This should only work on ballots that have NOT been cast. If a
    ballot has already been cast, it cannot be invalidated.

    If the ballot does not exist or has already been cast, this method will return false.

    :returns: If the ballot does not exist or has already been cast, will return Boolean FALSE.
              Otherwise will return Boolean TRUE.
    """
    # TODO: Implement this!
    store = VotingStore.get_instance()

    # Check if the ballot exists
    ballot = store.get_ballot(ballot_number)
    if not ballot:
        return False  # Ballot does not exist

    # Check if the ballot has already been cast
    if ballot.is_cast:
        return False  # Ballot has already been cast

    # Invalidate the ballot
    store.invalidate_ballot(ballot_number)
    return True


    #raise NotImplementedError()


def verify_ballot(voter_national_id: str, ballot_number: str) -> bool:
    """
    Verifies the following:

    1. That the ballot was specifically issued to the voter specified
    2. That the ballot is not invalid

    If all of the points above are true, then returns Boolean True. Otherwise returns Boolean False.

    :param: voter_national_id The id of the voter about to cast the ballot with the given ballot number
    :param: ballot_number The ballot number of the ballot that is about to be cast by the given voter
    :returns: Boolean True if the ballot was issued to the voter specified, and if the ballot has not been marked as
              invalid. Boolean False otherwise.
    """
    # TODO: Implement this!

    store = VotingStore.get_instance()

    # Check if the ballot exists
    ballot = store.get_ballot(ballot_number)
    if not ballot:
        return False  # Ballot does not exist

    # Check if the ballot is issued to the specified voter
    if ballot.voter_national_id != voter_national_id:
        return False  # Ballot is not issued to the specified voter

    # Check if the ballot is invalid
    if ballot.is_invalid:
        return False  # Ballot is invalid

    return True

    #raise NotImplementedError()


#
# Aggregate API
#

def get_all_ballot_comments() -> Set[str]:
    """
    Returns a list of all the ballot comments that are non-empty.
    :returns: A list of all the ballot comments that are non-empty
    """
    # TODO: Implement this!

    store = VotingStore.get_instance()
    return store.get_all_ballot_comments()

    #raise NotImplementedError()


def compute_election_winner() -> Candidate:
    """
    Computes the winner of the election - the candidate that gets the most votes (even if there is not a majority).
    :return: The winning Candidate
    """
    # TODO: Implement this!

    store = VotingStore.get_instance()
    return store.compute_election_winner()
    #raise NotImplementedError()


def get_all_fraudulent_voters() -> Set[str]:
    """
    Returns a complete list of voters who committed fraud. For example, if the following committed fraud:

    1. first: "John", last: "Smith"
    2. first: "Linda", last: "Navarro"

    Then this method would return {"John Smith", "Linda Navarro"} - with a space separating the first and last names.
    """
    # TODO: Implement this!

    store = VotingStore.get_instance()
    return store.get_all_fraudulent_voters()

    #raise NotImplementedError()
