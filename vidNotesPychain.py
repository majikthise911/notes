""" Hello everyone, My name is jordan clayton from Freqs and today I am going to walk through how to create an advancedc blockchain. 
This will be part 1 of a two part series. Part 2 will pick up exactly where part 1 left off.





We are going to follow a few main steps during this process

Steps: 

1.   will be to create a record data class 
    1.  Create a new data class named `Record`. This class will serve as the
        blueprint for the financial transaction records that the blocks of the ledger
        will store.
        
2.  modify the existing block data class to store record data 
    1.  we will Change the existing `Block` data class by replacing the generic `data`
        attribute with a `record` attribute that’s of type `Record`.
        
3.  add relevant user inputs to the streamlit interface 
    1.  Create additional user input areas in the Streamlit application. These
        input areas should collect the relevant information for each financial record
        that you’ll store in the `PyChain` ledger.
        
4.  test the PyChain Ledger by storing records """

# The very first thing we need to do is enter our dev environment with all the necessary packages installed. 
# # We can do this by running the following command in our terminal: and on to the second first most important 
# step in any pythonic adventure which is to import all the necessary packages.

################################################################################
# Imports
import streamlit as st # streamlit is a python library that allows you to create web apps
from dataclasses import dataclass # dataclasses are a way to create classes that are used to store data
from typing import Any, List # typing is a python library that allows you to define the type of data that is stored in a variable
import datetime as datetime # datetime is a python library that allows you to work with dates and times
import pandas as pd
import hashlib  # hashlib is a python library that allows you to hash data
from numpy import record    

################################################################################

### COPY PASTE ###
import streamlit as st 
from dataclasses import dataclass 
from typing import Any, List 
import datetime as datetime 
import pandas as pd
import hashlib  
from numpy import record    


# Step 1:

# Create a Record Data Class that consists of the `sender`, `receiver`, and
# `amount` attributes
@dataclass # add the @dataclass decorator immediately before the `Record` class definition. This essentially wraps our class 
           # in a function and gives it some extra functionality. This is a shortcut to bootstrap a class
class Record: # define a new class named Record
    sender: str # Add an attribute named sender of type str
    receiver: str # Add an attribute named receiver of type str
    amount: float # Add an attribute named amount of type float


################################################################################
# Step 2:
# Modify the Existing Block Data Class to Store Record Data

@dataclass # add the @dataclass decorator immediately before the `Block` class definition
class Block: # define a new class named Block
     # set it to a new Record class that we created in the previous section
    record: Record
    # Add an attribute named creator_id of type int
    creator_id: int 
    # create prev_hash attribute and set it to "0" to store the hash of the previous block in the chain
    prev_hash: str = "0" 
    # Add an attribute named timestamp of type str and set it to the current time
    timestamp: str = datetime.datetime.utcnow().strftime("%H:%M:%S") 
     # Add an attribute named nonce of type int and set it to 0. 
    # nonce stands for number only used once and is used to make sure that the hash of the block is unique
    nonce: int = 0 
# here we will create a function that will allow us to hash the block


# define a new function named hash_block and pass self as a parameter.  
# the self parameter refers the function back to the class that the function is nested within 
    def hash_block(self): 
        # Add an instance of the `sha256` hashing function
        sha = hashlib.sha256()   
        
        #record
        # self.record tells the function
        # to look at the record attribute of the block class and then encode it with the encode function.
        record = str(self.record).encode()  
        # Update the encoded record data with the hashing function. show what sha is above 
        sha.update(record) 
        
        #creator_id
        # encode the class "block"'s creator_id attribute
        creator_id = str(self.creator_id).encode() 
        # Update the encoded creator_id data with the hashing function
        sha.update(creator_id) 
        #prev_hash
        # encode the class "block"'s prev_hash attribute
        prev_hash = str(self.prev_hash).encode() 
        sha.update(prev_hash)

        #timestamp
        # encode the block's timestamp attribute
        timestamp = str(self.timestamp).encode() 
        # update the encoded timestamp data with the hashing function
        sha.update(timestamp) 
        #nonce
        # encode the block's nonce attribute
        nonce = str(self.nonce).encode()
        # update the encoded nonce data with the hashing function
        sha.update(nonce)  

        # return the hashes of all the block class attributes
        return sha.hexdigest() 

""" Now we will create a new class named PyChain that will store all of the blocks in the chain. 
PyChain is a fully parallelized PyTorch implementation of end-toend lattice-free maximum mutual information trainng 
for chain models in the Kaldi automatic speech recognition ASR toolkit
I will not pretend to understand all of the words that I just spoke, but I will say that this class will store all of the blocks in the chain
and will allow us to add new blocks to the chain """

@dataclass
class PyChain:
    # Chain: List[Block] means that the chain attribute of the PyChain class will be a list of Block objects
    chain: List[Block] 
    # Add an attribute named difficulty of type int and set it to 4. This will be our default difficulty level
    difficulty: int = 4 

# define a new function named proof_of_work and pass self and block as parameters
    def proof_of_work(self, block): 
        # create a variable named calculated_hash and set it to the hash of the block
        calculated_hash = block.hash_block() 
        # create a variable named num_of_zeros and set it to the difficulty level of the chain
        # what we are saying here is that we want the hash of the block to start with a certain number of 
        # zeros equal to the difficulty level of the chain
        num_of_zeros = "0" * self.difficulty 


        # while the calculated hash does not start with the 
        # number of zeros equal to the difficulty level
        #nonce will keep counting until there is a winning hash
        while not calculated_hash.startswith(num_of_zeros): 
            block.nonce +=1 
            # and then we recalculate the hash of the block each time the nonce is incremented
            calculated_hash = block.hash_block() 
        
        # once we have a hash that starts with the number of zeros equal to the difficulty level
        # we print the winning hash. notice this line is outside of the while loop
        print("Winning Hash", calculated_hash) 
        return block 

    # this is where we are going to start the process of adding the new block to the chain
    def add_block(self, candidate_block): 
        # create a variable named block and set it to the result of the proof_of_work function
        block = self.proof_of_work(candidate_block) 
        # add the block to the chain. use the += operator to add the block to the chain
        self.chain += [block] 
""" 
    This next block of code is where we will be validating the chain 
        We will be validating the integrity of the PyChain by
        comparing the calculated hash code of each block to the `prev_hash`
        value contained in the following block
        Add the code to generate the hash of the first block in the chain.
        Set the hash equal to a variable called block_hash
        Note: The first block in the chain is at index position 0. """

    def is_valid(self):
        block_hash = self.chain[0].hash_block() #hash the first block in the chain  

        # Now we create a for-loop to access the remainder of the blocks in the
        # chain, starting at index position 1


        #the remainder of the blocks in the chain, starting from index 1
        for block in self.chain[1:]: 

            # Code an if statement that compares the block_hash of the
            # previous block to the prev_hash value of the current block
            # If the two hashes are NOT equal, print a statement that says
            # "Blockchain is invalid", and then return the value False

            if block_hash != block.prev_hash:  
                print("Blockchain is invalid")
                return False

        # Set the block_hash value equal to the hashed value of the current

            block_hash = block.hash_block()
        
        print("Blockchain is valid")
        return True

################################################################################
# Step 3:

""" Add Relevant User Inputs to the Streamlit Interface
Code additional input areas for the user interface of your Streamlit
application. Create these input areas to capture the sender, receiver, and
amount for each transaction that you’ll store in the `Block` record.
To do so, complete the following steps:
1. Add an input area where you can get a value for `sender` from the user.
2. Add an input area where you can get a value for `receiver` from the user.
3. Add an input area where you can get a value for `amount` from the user.
4. As part of the Add Block button functionality, update `new_block` so that 
`Block` consists of an attribute named `record`, which is set equal to a `Record` 
 that contains the `sender`, `receiver`, and `amount` values. The updated `Block`should also 
 include the attributes for `creator_id` and `prev_hash`.
 Since this video is really more on the technical side, I will not be going into detail 
 on how to add the input areas to the Streamlit interface.
 """

# Streamlit Code

# Add the cache decorator for Streamlit
# allow output mutation is set to true because we are going to be changing the chain
@st.cache(allow_output_mutation=True) 
def setup():
    print("Initializing Chain")
    # create a new instance of the PyChain class and pass it a list of Block objects. 
    # the first block in the list is the genesis block
    return PyChain([Block("Genesis", 0)]) 


st.markdown("# PyChain")
st.markdown("## Store a Transaction Record in the PyChain")

pychain = setup()

################################################################################


# Add an input area where you can get a value for `sender` from the user.
sender = st.text_input("Sender Info")

# Add an input area where you can get a value for `receiver` from the user.
receiver = st.text_input("Receiver Info")


# Add an input area where you can get a value for `amount` from the user.
amount = st.number_input("Amount")

if st.button("Add Block"):
    # get the last block in the chain
    prev_block = pychain.chain[-1] 
    # get the hash of the last block in the chain
    prev_block_hash = prev_block.hash_block() 
 
    # Update `new_block` so that `Block` consists of an attribute named `record`
    # which is set equal to a `Record` that contains the `sender`, `receiver`,
    # and `amount` values
    new_block = Block(
        record = Record,
        # this is the id of the creator of the block. 42 is the answer to life, the universe, and everything
        creator_id=42, 
        prev_hash=prev_block_hash
    )

    pychain.add_block(new_block)
    st.balloons()
################################################################################
# Streamlit Code (continues)

st.markdown("## The PyChain Ledger")

pychain_df = pd.DataFrame(pychain.chain).astype(str)
st.write(pychain_df)

difficulty = st.sidebar.slider("Block Difficulty", 1, 5, 2) # block difficulty slider of min value, max value, and starting value 
pychain.difficulty = difficulty # set the difficulty of the chain to the value of the slider

st.sidebar.write("# Block Inspector")
selected_block = st.sidebar.selectbox(
    "Which block would you like to see?", pychain.chain
)

st.sidebar.write(selected_block)

if st.button("Validate Chain"):
    st.write(pychain.is_valid())

################################################################################
# Step 4:
# Test the PyChain Ledger by Storing Records

# Test your complete `PyChain` ledger and user interface by running your
# Streamlit application and storing some mined blocks in your `PyChain` ledger.
# Then test the blockchain validation process by using your `PyChain` ledger.
# To do so, complete the following steps:

# 1. In the terminal, navigate to the project folder where you've coded the
#  Challenge.

# 2. In the terminal, run the Streamlit application by
# using `streamlit run pychain.py`.

# 3. Enter values for the sender, receiver, and amount, and then click the "Add
# Block" button. Do this several times to store several blocks in the ledger.

# 4. Verify the block contents and hashes in the Streamlit drop-down menu.
# Take a screenshot of the Streamlit application page, which should detail a
# blockchain that consists of multiple blocks. Include the screenshot in the
# `README.md` file for your Challenge repository.

# 5. Test the blockchain validation process by using the web interface.
# Take a screenshot of the Streamlit application page, which should indicate
# the validity of the blockchain. Include the screenshot in the `README.md`
# file for your Challenge repository.
