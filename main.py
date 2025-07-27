from typing import Dict, Tuple, List, Generator, Set

def parse_txid(txid: str) -> tuple:
    """
    Converts a hexadecimal txid string into a tuple of byte pairs.
    Example: 'deadbeef' -> ('de', 'ad', 'be', 'ef')
    """
    # TODO: Return a tuple of 2-character segments from txid
    return tuple(txid[i:i+2] for i in range(0, len(txid), 2))

def create_utxo(txid: str, vout: int, amount: int) -> dict:
    """
    Creates a dictionary representing a UTXO with the given txid, vout, and amount.
    """
    # TODO: Return a dict with keys 'txid', 'vout', and 'amount'
    return {"txid": txid, "vout": vout, "amount": amount}

def update_utxo(utxo: dict, new_amount: int) -> None:
    """
    Updates the 'amount' field in a UTXO dictionary to a new value.
    """
    # TODO: Use update to set new 'amount'
    utxo.update({"amount": new_amount})

def unpack_utxo(utxo: dict) -> str:
    """
    Unpacks a UTXO dictionary and returns a formatted string representation.
    """
    txid = utxo.get("txid")
    vout = utxo.get("vout")
    amount = utxo.get("amount")
    return f"UTXO - TXID: {txid}, VOUT: {vout}, AMOUNT: {amount}"

def swap_addresses(addr1: str, addr2: str) -> tuple:
    """
    Swaps two Bitcoin addresses and returns them in reversed order.
    """
    # TODO: Swap the values and return as tuple
    return (addr2, addr1)

def unique_addresses(addresses: list) -> set:
    """
    Returns a set of unique Bitcoin addresses from the provided list.
    """
    # TODO: Convert the list to a set
    return set(addresses)

class BitcoinWallet:
    def __init__(self):
        """
        Initializes the wallet with an empty UTXO set.
        """
        self.utxos: Dict[str, dict] = {}
    
    def add_utxo(self, utxo: Dict) -> None:
        """
        Adds a UTXO to the wallet using a unique txid:vout key.
        """
        # TODO: Create key from 'txid' and 'vout', store UTXO in self.utxos
        key = f"{utxo['txid']}:{utxo['vout']}"
        self.utxos[key] = utxo
    
    def get_balance(self) -> float:
        """
        Returns the total balance of all UTXOs in the wallet.
        """
        # TODO: Sum the 'amount' of all UTXOs
        return sum(utxo['amount'] for utxo in self.utxos.values())

class TransactionPool:
    def __init__(self):
        """
        Initializes an empty transaction pool.
        """
        self.tx_pool: Set[str] = set()
    
    def add_transaction(self, txid: str) -> bool:
        """
        Adds a txid to the transaction pool.
        Returns True if it was not already present, False otherwise.
        """
        # TODO: Check for presence and add if not present
        if txid not in self.tx_pool:
            self.tx_pool.add(txid)
            return True
        return False
    
    def get_pool_size(self) -> int:
        """
        Returns the total number of unique transactions in the pool.
        """
        # TODO: Return length of tx_pool
        return len(self.tx_pool)

def block_height_generator(start: int, end: int) -> Generator[int, None, None]:
    """
    Yields block heights from start to end (exclusive).
    """
    # TODO: Use a generator loop to yield block heights
    for height in range(start, end):
        yield height