"""This file contains functions to get all info from json files """


# get all info about user's tasks and put it in the global structure
def get_all_tasks_info(tasks_list, users_list, all_users_info):
    for user in users_list:
        completed_task_list = []
        remain_task_list = []
        for task in tasks_list:
            try:
                if task["userId"] == user["id"]:
                    if task["completed"]:
                        completed_task_list.append(task["title"])
                    else:
                        remain_task_list.append(task["title"])
            except KeyError as exc:
                pass
        all_users_info[user["id"]] = {}
        all_users_info[user["id"]]["amount"] = len(completed_task_list) + \
                                               len(remain_task_list)
        all_users_info[user["id"]]["compl_tasks"] = completed_task_list
        all_users_info[user["id"]]["compl_amount"] = len(completed_task_list)
        all_users_info[user["id"]]["remain_tasks"] = remain_task_list
        all_users_info[user["id"]]["remain_amount"] = len(remain_task_list)
    return all_users_info


# get info from the list "search_info" and put it in the global structure
def get_personal_info(users_list, all_users_info, search_info):
    for user in users_list:
        try:
            all_users_info[user["id"]][search_info] = user[search_info]
        except KeyError as exc:
            pass


# get company name and put it in the global structure
def get_company_name(users_list, all_users_info):
    for user in users_list:
        try:
            all_users_info[user["id"]]["company"] = user["company"]["name"]
        except KeyError as exc:
            pass
