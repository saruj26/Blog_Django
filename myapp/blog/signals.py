from django.contrib.auth.models import Group,Permission

def create_groups_permissions(sender,**kwargs):
    # create groups
    try :
        readers_group,created = Group.objects.get_or_create(name="Readers")
        authors_group,created = Group.objects.get_or_create(name="Authors")
        editors_group,created = Group.objects.get_or_create(name="Editors")

        #create permissions
        readers_permissions = [
            Permission.objects.get(codename = 'view_post')

        ]

        authors_permissions=[
        Permission.objects.get(codename = 'add_post'),
        Permission.objects.get(codename = 'change_post'),
        Permission.objects.get(codename = 'delete_post'),
        ]


        can_publish,created = Permission.objects.get_or_create(codename = 'can_publish' , content_type_id =7, name= "can publish post")

        editors_permissions = [
            can_publish,
            Permission.objects.get(codename = 'add_post'),
            Permission.objects.get(codename = 'change_post'),
            Permission.objects.get(codename = 'delete_post'),
        ]   

        # assigning the permissions to group
        readers_group.permissions.set(readers_permissions)
        authors_group.permissions.set(authors_permissions)
        editors_group.permissions.set(editors_permissions)
        
    except Exception as e:
        print(f"An error occured {e} ")


    print("Groups and Permissions Created successfully")