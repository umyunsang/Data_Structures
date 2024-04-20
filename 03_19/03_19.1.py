from singlelist import SingleList as sl

slist = sl()

slist.create_head()

slist.node_append("park")
slist.node_append("choi")
slist.node_append("lee")
slist.node_insert("chol","hwang")

slist.all_print()

