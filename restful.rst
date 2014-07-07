
����ÿ��topic������"mysql vs oracle vs mssql"
�û�ֻ�ܷ���һ��document�������û����Զ�document�������ۣ����۴���������

=========================================================================================
register                        							|post    /users/_register -d jsondata
login                              							|post    /users/_login -d jsondata()
logout                             							|post    /users/_logout -d jsondata
search user                    								|post    /users/_search -d jsondata
active user(������֤����)          							|post    /users/_active -d jsondata
upload face													|post 	 /users/_uploadface -d
����<=4M

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
'title':'������ϵ�����ݿ�Ƚ�', <= 1024 bytes
'type':'�������ͣ�����',
'items':
{
'mysql':'xxxxbrief',<=1024 bytes
'oracle':'xxxxbrief'<=1024 bytes
},
'fields':['д���ٶ�','��ȡ�ٶ�','�ȶ���','��������'] every field length <= 32 bytes
'document_max_length':1024/4096/8192
}

---------------------
delete topic(only admin right)                              |delete /topics/topicid
---------------------
follow topic                                                |put    /topics/topicid/_follow
---------------------
unfollow topic                 								|put    /topics/topicid/_unfollow
---------------------
score topic(����)                    						|put    /topic/topicid/_score
---------------------
get topic content											|get    /topics/topicid
---------------------
get topic documents											|get    /topics/topicid/documents?startidx=&number=

=========================================================================================
create document              								|post   /topic/topicid/documents -d
update document									            |put    /topics/topicid/documents/documentid -d
'content':<=limited length(���ݴ�������ʱ��document_max_lengt����)

---------------------
delete document									            |delete /topic/topicid/documents/documentid
---------------------
score document(����)             							|put    /topic/topicid/documents/documentid/_score
--------------------
list document comments          							|get    /topic/topicid/documents/documentid?startidx=&number=

=========================================================================================
create comment             								    |post   /topic/topicid/documents/documentid/comments -d
update comment									            |put    /topics/topicid/documents/documentid/comments/commentid -d
'content':'' <=0x100 bytes

---------------------
delete comment									            |delete /topic/topicid/documents/documentid/comments/commentid
---------------------
score comment(����)             							|put    /topic/topicid/documents/documentid/comments/commentid/_score -d
