'''
TPRG 2131 Fall 2024 Project 1, Test file template.
Nov, 2024
Hemil Prajapati (100942152).
This program is strictly my own work. Any material
beyond course learning materials that is taken from
the Web or other sources is properly cited, giving.
credit to the original author(s).

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
    vending.event = '$2' # a twonie
    vending.update()
    assert vending.state.name == 'add_coins'
    assert vending.amount == 200
    
    vending.event = '$1' # loonie
    vending.update()
    assert vending.state.name == 'add_coins'
    assert vending.amount == 300
    
    vending.event = '25¢' # quarter
    vending.update()
    assert vending.state.name == 'add_coins'
    assert vending.amount == 325
    
    vending.event = '10¢' # dime
    vending.update()
    assert vending.state.name == 'add_coins'
    assert vending.amount == 335
    
    vending.event = '5¢' # nickel
    vending.update()
    assert vending.state.name == 'add_coins'
    assert vending.amount == 340
