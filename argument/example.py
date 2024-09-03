def example_all(name, *flowers, **costs):
    """
    :param name: 이름
    :param flowers: 꽃
    :param costs: 비용
    """
    print(name)
    for flower in flowers:
        print(flower)
    for c, costs in costs.items():
        print(c, '비용은', costs)

my_name = '다연'
flower1 = 'rose'
flower2 = 'lily'
flower3 = 'sunflower'

# help(example_all)
example_all(my_name, flower1, flower2, flower3, 장미=10, 백합=20, 해바라기=30)