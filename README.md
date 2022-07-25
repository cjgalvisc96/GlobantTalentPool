# GlobantTalentPool

#  Python

  ### Even loop
  The event loop is the core of every asyncio application. Event loops run asynchronous tasks and callbacks, perform network IO operations, and run subprocesses
  ```(python3)
  import asyncio

  async def main():
    print('hello')
    await asyncio.sleep(1)
    print('world')

  asyncio.run(main())
  >>> hello
  >>> world
  ```
  ### Store collections
  **List, Set, Dictionary and Tuple**

  ### List
  * Lists are used to store multiple items in a single variable.
  * List items are ordered, changeable(we can change, add, and remove items in a list after it has been created), and allow duplicate values.
  * List items can be of any data type.
  * There are some list methods that will change the order, but in general: the order of the items will not change.
    
  ```(python3)
  list_one = ["abc", 34, True, 40, "male"]
  ```

  ### Dictionary 
  * Dictionary items are ordered(pyton3.7>), changeable, and does not allow duplicates.
  * When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.
  * Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.
  * Dictionaries cannot have two items with the same key
  ```(python3)
  thisdict =	{
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
  }
  ```

  ###  Tuples
  * Tuple items are ordered, unchangeable(inmutable), and allow duplicate values.
  * When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.
  * Tuples are unchangeable(inmutable), meaning that we cannot change, add or remove items after the tuple has been created.
  * Since tuples are indexed, they can have items with the same value
  * The tuples are more faster and using less memory than the lists
  ```(python3)
  thistuple_one = ("carl",)
  thistuple_two = ("apple", "banana", "cherry", "apple)
  ```

  ### Sets
  * A set is a collection which is unordered, unchangeable*, and unindexed.
  * Once a set is created, you cannot change its items, but you can remove items and add new items.
  * Set items can appear in a different order every time you use them, and cannot be referred to by index or key.
  * Sets cannot have two items with the same value.
  ```(python3)
  thisset = {"apple", "banana", "cherry"}
  ```

  ###  Generators and Iterators 
  In summary: Iterators are objects that have an ___iter__ and a ___next__ (next in Python 2) method. Generators provide an easy, built-in way to create instances of Iterators.

  A function with *yield* in it is still a function, that, when called, returns an instance of a generator object:
  ```(python3)
  # Fisrt way to create a generator
  def generator_function(start, stop):
    for i in range(start, stop):
        yield i * i
   
  # Second way to create a generator
  a_generator = (i for i in range(0))

  class YesIterator(collections.Iterator):

    def __init__(self, stop):
        self.x = 0
        self.stop = stop

    def __iter__(self):
        return self

    def next(self):
        if self.x < self.stop:
            self.x += 1
            return 'yes'
        else:
            raise StopIteration
  ```
  ###  Context_manager
  [Code Link](./study/context_manager.py)

  ### Decorators 
  [Code Link](./study/decorators.py)

  ###  Lambda ó anonymous functions
  * A lambda function is a small anonymous function
  * A lambda function can take any number of arguments, but can only have one **expression**.
  * The power of lambda is better shown when you use them as an anonymous function inside another function.
  ```(python3)
  # lambda arguments : expression
  def myfunc(n):
    return lambda a : a * n

  mydoubler = myfunc(2)

  print(mydoubler(11))
  ```
  ###  List Comprehension 
  * List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
  
  * Without list comprehension you will have to write a **for** statement with a conditional test inside.
  ```(python3)
  #  newlist = [expression for item in iterable if condition == True] 
  fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
  newlist = [x for x in fruits if "a" in x]
  ```
  ###  *args y kwargs
Special Symbols Used for passing arguments:

    *args (Non-Keyword Arguments)
    **kwargs (Keyword Arguments)
  We use the “wildcard” or “*” notation like this – *args OR **kwargs – as our function’s argument when we have doubts about the number of  arguments we should pass in a function
  ```(python3)
  def myFun(*argv):
    for arg in argv:
        print(arg)

  def myFun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))
  ```

#  Django
  ###  What are the Mixins ?
  Are classes which contains a combination of methods from other classe
#  Django rest framework
  ###  funciones basadas en funciones (@api_view)
  REST framework also allows you to work with regular function based views. It provides a set of simple decorators that wrap your function based views to ensure they receive an instance of Request (rather than the usual Django HttpRequest) and allows them to return a Response (instead of a Django HttpResponse), and allow you to configure how the request is processed.
  
  ```(python3)
  from rest_framework.decorators import api_view
  from rest_framework.response import Response

  @api_view()
  def hello_world(request):
      return Response({"message": "Hello, world!"})
  ```

  ###  funciones basadas en vistas [ APIVIEW (get, post..), genericsViews(ListAPIView,...)]
  REST framework provides an APIView class, which subclasses Django's View class.
  ```(python3)
  from rest_framework.views import APIView
  from rest_framework.response import Response
  from rest_framework import authentication, permissions
  from django.contrib.auth.models import User

  class ListUsers(APIView):
      authentication_classes = [authentication.TokenAuthentication]
      permission_classes = [permissions.IsAdminUser]

      def get(self, request, format=None):
          usernames = [user.username for user in User.objects.all()]
          return Response(usernames)
   ```
#  mongo
  ###  bulk operations
  The MongoDB bulk methods are used to perform bulk operation like bulk write and bulk remove.
  ```(mongo)
  var bulk = db.items.initializeUnorderedBulkOp();
  bulk.insert( { item: "abc123", defaultQty: 100, status: "A", points: 100 } );
  bulk.insert( { item: "ijk123", defaultQty: 200, status: "A", points: 200 } );
  bulk.insert( { item: "mop123", defaultQty: 0, status: "P", points: 0 } );
  bulk.execute();
  ```
  ###  Index in MongoDB
MongoDB uses indexing in order to make the query processing more efficient. If there is no indexing, then the MongoDB must scan every document in the collection and retrieve only those documents that match the query. Indexes are special data structures that stores some information related to the documents such that it becomes easy for MongoDB to find the right data file. The indexes are order by the value of the field specified in the index. 
  

  ```(mongo)
  db.products.createIndex(
    { item: 1, quantity: -1 } ,
    { name: "query for inventory" }
  )
  ```