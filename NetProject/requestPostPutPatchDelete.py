import requests as req


## GET Example:
myGetUrl = "https://jsonplaceholder.typicode.com/todos"
response = req.get(myGetUrl)
print(response.json())



## POST Example:
myToDo = {
    "userId": 2,
    "title": "try first post",
    "completed": False
}
MyPostUrl = "https://jsonplaceholder.typicode.com/todos"
post_response = req.post(MyPostUrl, json=myToDo)
print(post_response.json()) 
      #{'userId': '2', 'title': 'try first post', 'completed': 'False', 'id': 201}



#PUT Example:
PutUrl = "https://jsonplaceholder.typicode.com/todos/2"
MyPut = {
    "userId": 2,
    "title": "try second put",
    "completed": False
}
MyPutUrl = req.put(PutUrl, json=MyPut)
print(MyPutUrl.json())
    #{'userId': 2, 'title': 'try second put', 'completed': False, 'id': 2}



 # PATCH Examples:
PatchUrl = "https://jsonplaceholder.typicode.com/todos/2"
MyPatch = {
    "title": "try last patch"
}   
MyPatchUrl = req.patch(PatchUrl, json=MyPatch)
print(MyPatchUrl.json())
    #{'userId': 2, 'title': 'try last patch', 'completed': False, 'id': 2}


# DELETE Example:
deleteUrl = "https://jsonplaceholder.typicode.com/todos/2"
myDelete = req.delete(deleteUrl)
print(myDelete.json())
    #{}  #Empty because the data has been deleted. only--> {}

