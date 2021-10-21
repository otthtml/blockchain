'''
Our server
'''
from blockchain import Blockchain
from flask_adapter import FlaskAdapter


app = FlaskAdapter().start_server()
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

blockchain = Blockchain()


@app.route('/mine_block', methods = ['GET'])
def mine_block():
    ''' endpoint for mining new blocks'''
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    block = blockchain.create_block(proof, previous_hash)
    response = {
        'message': 'You just mined a block',
        'index': block['index'],
        'timestamp': block['timestamp'],
        'proof': str(block['proof']),
        'previous_hash': str(block['previous_hash'])
    }
    return FlaskAdapter().json_response(response), 201

@app.route('/get_chain', methods = ['GET'])
def get_chain():
    '''endpoint that returns the entire blockchain'''
    response = {
        'chain': str(blockchain.chain),
        'length': len(blockchain.chain)
    }
    return FlaskAdapter().json_response(response), 200


if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = '5000', debug = True)
