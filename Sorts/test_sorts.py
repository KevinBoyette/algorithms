from bubble_sort import bubble_sort
from insertion_sort import insertion_sort
from selection_sort import selection_sort

def setup_module(module):
    print ("setup_module      module:%s" % module.__name__)

def teardown_module(module):
    print ("teardown_module   module:%s" % module.__name__)

def setup_function(function):
    print ("setup_function    function:%s" % function.__name__)

def teardown_function(function):
    print ("teardown_function function:%s" % function.__name__)


class TestBubbleSort:
    def setup(self):
        print ("setup             class:TestStuff")

    def teardown(self):
        print ("teardown          class:TestStuff")

    def setup_class(cls):
        print ("setup_class       class:%s" % cls.__name__)

    def teardown_class(cls):
        print ("teardown_class    class:%s" % cls.__name__)

    def setup_method(self, method):
        print ("setup_method      method:%s" % method.__name__)

    def teardown_method(self, method):
        print ("teardown_method   method:%s" % method.__name__)

    def test_bubble_sort_empty(self):
        assert bubble_sort([]) == []

    def test_bubble_sort_with_one_item(self):
        assert bubble_sort([1]) == [1]
        assert bubble_sort([1]) != [1, 2]

    def test_bubble_sort_with_many_values(self):
        assert bubble_sort([2,1,2,4,3,2]) != []
        assert bubble_sort([2,1,2,4,3,2]) == [1,2,2,2,3,4]


class TestInsertionSort:
    def setup(self):
        print ("setup             class:TestStuff")

    def teardown(self):
        print ("teardown          class:TestStuff")

    def setup_class(cls):
        print ("setup_class       class:%s" % cls.__name__)

    def teardown_class(cls):
        print ("teardown_class    class:%s" % cls.__name__)

    def setup_method(self, method):
        print ("setup_method      method:%s" % method.__name__)

    def teardown_method(self, method):
        print ("teardown_method   method:%s" % method.__name__)

    def test_insertion_sort_empty(self):
        assert insertion_sort([]) == []

    def test_insertion_sort_with_one_item(self):
        assert insertion_sort([1]) == [1]
        assert insertion_sort([1]) != [1, 2]

    def test_insertion_sort_with_many_values(self):
        assert insertion_sort([2,1,2,4,3,2]) != []
        assert insertion_sort([2,1,2,4,3,2]) == [1,2,2,2,3,4]


class TestselectionSort:
    def setup(self):
        print ("setup             class:TestStuff")

    def teardown(self):
        print ("teardown          class:TestStuff")

    def setup_class(cls):
        print ("setup_class       class:%s" % cls.__name__)

    def teardown_class(cls):
        print ("teardown_class    class:%s" % cls.__name__)

    def setup_method(self, method):
        print ("setup_method      method:%s" % method.__name__)

    def teardown_method(self, method):
        print ("teardown_method   method:%s" % method.__name__)

    def test_selection_sort_empty(self):
        assert selection_sort([]) == []

    def test_selection_sort_with_one_item(self):
        assert selection_sort([1]) == [1]
        assert selection_sort([1]) != [1, 2]

    def test_selection_sort_with_many_values(self):
        assert selection_sort([2,1,2,4,3,2]) != []
        assert selection_sort([2,1,2,4,3,2]) == [1,2,2,2,3,4]
