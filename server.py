'''
Our server
'''
from flask.json import jsonify
from blockchain import Blockchain
from flask_adapter import FlaskAdapter


app = FlaskAdapter().start_server()

blockchain = Blockchain()


@app.route('/mine_block', methods = ['GET'])
def mine_block():
    '''
    endpoint for mining new blocks
    '''
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    block = blockchain.create_block(proof, previous_hash)
    response = {
        'message': 'You just mined a block',
        'index': block['index'],
        'timestamp': block['timestamp'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash']
    }
    return jsonify(response), 201
