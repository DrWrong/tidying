
对于每个topic，比如"mysql vs oracle vs mssql"
用户只能发表一次document，其他用户可以对document发表评论，评论次数不限制

=========================================================================================
register                        							|post    /users/_register -d jsondata
login                              							|post    /users/_login -d jsondata()
logout                             							|post    /users/_logout -d jsondata
search user                    								|post    /users/_search -d jsondata
active user(邮箱验证激活)          							|post    /users/_active -d jsondata
upload face													|post 	 /users/_uploadface -d
限制<=4M

change preferred language     								|put 	 /_language -d "language="
=========================================================================================
get user info                      							|get     /users/userid
update user                        							|post    /users/userid -d
user talk to user                  							|post    /users/userid/_msg -d "msg="
user recv from user                							|get     /users/userid/_msg
heartbeat(user online)                         				|post    /users/userid/_heartbeat
follow user                              					|post    /users/userid/_follow
unfollow user                          						|post    /users/userid/_unfollow
list users'documents										|get     /users/userid/documents?orderby=optionalvalue
list users'fans                      						|get     /users/userid/fans
list users'concerns                             			|get     /users/userid/concerns

list all comments for user                  				|get     /users/userid/comments
create comment to user                          			|post    /users/userid/comments -d
delete comment for user   									|delete  /users/userid/comments/commentid


=========================================================================================
list all topics                                             |get    /topics?startidx=&number=
if user has logined:list this user preferred topics

---------------------
search topic												|get    /topics/_search?key=key1 key2
---------------------
create topic(only admin right)                              |post   /topics -d
update topic(only admin right)                              |put    /topics/topicid -d
{
'title':'主流关系型数据库比较', <= 1024 bytes
'type':'主题类型，保留',
'items':
{
'mysql':'xxxxbrief',<=1024 bytes
'oracle':'xxxxbrief'<=1024 bytes
},
'fields':['写入速度','读取速度','稳定性','备份能力'] every field length <= 32 bytes
'document_max_length':1024/4096/8192
}

---------------------
delete topic(only admin right)                              |delete /topics/topicid
---------------------
follow topic                                                |put    /topics/topicid/_follow
---------------------
unfollow topic                 								|put    /topics/topicid/_unfollow
---------------------
score topic(点赞)                    						|put    /topic/topicid/_score
---------------------
get topic content											|get    /topics/topicid
---------------------
get topic documents											|get    /topics/topicid/documents?startidx=&number=

=========================================================================================
create document              								|post   /topic/topicid/documents -d
update document									            |put    /topics/topicid/documents/documentid -d
'content':<=limited length(根据创建主题时，document_max_lengt设置)

---------------------
delete document									            |delete /topic/topicid/documents/documentid
---------------------
score document(点赞)             							|put    /topic/topicid/documents/documentid/_score
--------------------
list document comments          							|get    /topic/topicid/documents/documentid?startidx=&number=

=========================================================================================
create comment             								    |post   /topic/topicid/documents/documentid/comments -d
update comment									            |put    /topics/topicid/documents/documentid/comments/commentid -d
'content':'' <=0x100 bytes

---------------------
delete comment									            |delete /topic/topicid/documents/documentid/comments/commentid
---------------------
score comment(点赞)             							|put    /topic/topicid/documents/documentid/comments/commentid/_score -d
