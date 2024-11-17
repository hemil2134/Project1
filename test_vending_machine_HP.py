'''
TPRG 2131 Fall 2024 Project 1, Test file template.
Nov, 2024


'''
from vending_machine_HP import VendingMachine, WaitingState, AddCoinsState, DeliverProductState, CountChangeState

def test_VendingMachine():
    # new machine object
    vending = VendingMachine()

    # Add the states - ORG
    # vending.add_state(WaitingState())
    # vending.add_state(CoinsState())
    # vending.add_state(DispenseState())
    # vending.add_state(ChangeState())

    # My revisions
    vending.add_state(WaitingState())
    vending.add_state(AddCoinsState())
    vending.add_state(DeliverProductState())
    vending.add_state(CountChangeState())


    # Reset state is "waiting for first coin"
    vending.go_to_state('waiting')
    assert vending.state.name == 'waiting'

    # test that the first coin causes a transition to 'coins'
    vending.event = '200' # a twonie
    vending.update()
    assert vending.state.name == 'add_coins'
    assert vending.amount == 200
    
    