import nni
def max_pool(k):
    pass

h_conv1 = 1
nni.choice({'foo': foo, 'bar': bar})(1)
conv_size = nni.choice({2: 2, 3: 3, 5: 5, 7: 7}, name='conv_size')
abc = nni.choice({'2': '2', 3: 3, '(5 * 6)': 5 * 6, 7: 7}, name='abc')
h_pool1 = nni.function_choice({'max_pool': lambda : max_pool(h_conv1),
    'h_conv1': lambda : h_conv1,
    'avg_pool': lambda : avg_pool(h_conv2, h_conv3)}
)
h_pool1 = nni.function_choice({'max_pool(h_conv1)': lambda : max_pool(
    h_conv1), 'avg_pool(h_conv2, h_conv3)': lambda : avg_pool(h_conv2,
    h_conv3)}, name='max_pool')
h_pool2 = nni.function_choice({'max_poo(h_conv1)': lambda : max_poo(h_conv1
    ), '(2 * 3 + 4)': lambda : 2 * 3 + 4, '(lambda x: 1 + x)': lambda : lambda
    x: 1 + x}, name='max_poo')
tmp = nni.qlognormal(1.2, 3, 4.5)
test_acc = 1
nni.report_intermediate_result(test_acc)
test_acc = 2
nni.report_final_result(test_acc)
