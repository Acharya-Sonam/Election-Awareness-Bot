import pytest
from modules.eligibility import is_eligible

def test_is_eligible():
    # Valid adult citizen
    assert is_eligible(18, "Yes") == True
    assert is_eligible(30, "Yes") == True
    
    # Underage citizen
    assert is_eligible(17, "Yes") == False
    assert is_eligible(0, "Yes") == False
    
    # Adult non-citizen
    assert is_eligible(18, "No") == False
    assert is_eligible(45, "No") == False
    
    # Underage non-citizen
    assert is_eligible(16, "No") == False
