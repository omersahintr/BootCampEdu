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

