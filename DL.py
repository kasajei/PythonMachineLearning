import pickle, gzip, numpy
import theano.tensor as T
import theano

# Load the dataset
f = gzip.open('data/mnist.pkl.gz', 'rb')
train_set, valid_set, test_set = pickle.load(f,encoding='latin1')
f.close()


def shared_dataset(data_xy):
    """
    """
    data_x, data_y = data_xy
    shared_x = theano.shared(numpy.asarray(data_x, dtype=theano.config.floatX))
    shared_y = theano.shared(numpy.asarray(data_y, dtype=theano.config.floatX))
    return shared_x, T.cast(shared_y, "int32")
    
test_set_x, test_set_y = shared_dataset(test_set)
valid_set_x, valid_set_y = shared_dataset(valid_set)
train_set_x, train_set_y = shared_dataset(train_set)

batch_size = 500

data = train_set_x[2*batch_size: 3*batch_size]
label = train_set_y[2*batch_size: 3*batch_size] 
