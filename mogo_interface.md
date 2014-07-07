1. user document
```json
	{
       _id: uuid(), //userid
       name: user nick name,
       thirdparty_token:
       {
           sina_token:
           github_token:
       }
       avator: 用户头像
       createtime: 
       logintime:
       password:
       email:
       sex:
       idiograph: 个人哲学
       money:
       score:
       identity: 管理员|普通用户
       language: 语言设置
       topic_score_list: [topicId] 点赞的话题数量
       topic_follow_list: [topicId]
       user_follow_list: [userId]
       documetn_score_list: [documentId] 点赞的documents 数量
    }
```

2. topic document:
```json
	{
    	_id: uuid
        languate:语言偏好
        userid: 发布者
        title: 
        type: 类型 保留
        description: 描述
        items:[] //话题对比的内容，至少两项
        fields:[] //投票的内容
        result://投票的结构
        { 
           key:{
                entry1:score1,
                entry2:score2,
               }
        }//注key为items中的值，entry为fields中的值 score为结果
        createtime:
        updatetime:
        totalscore: 总得分 点赞数 + document 数 + comment 数  
    }
```

3. documents document:
```json
	{
       _id:
       topicid:
       updatetime: 
       authorid: Uid
       topicid: topicid
       content:
       totalscore: 总得分 点赞数 + 评论数
    }
```
4. comment document:
```json
	{
      _id:
      authorid: 评论作者
      body: @topicauthorid hello123
      createtime:
    }
```
