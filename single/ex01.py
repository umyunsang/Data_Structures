from singlelist import SingleList as sl

slist = sl()
slist.create_head()

slist.node_append("1")
slist.node_append("2")
slist.node_append("3")
slist.node_append("5")
slist.node_append("6")
slist.node_append("7")

slist.node_edit("2","4")
slist.node_delete("6")
slist.node_find("5")

slist.all_print()
