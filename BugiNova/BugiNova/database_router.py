class AppDatabaseRouter:
    """
    A router to control which app's models go to which database.
    """

    def db_for_read(self, model, **hints):
        if model._meta.app_label in ['user_management', 'bug_management', 'project_management',
                                     'component_management', 'notification_management', 'attachment_management']:
            return model._meta.app_label + '_db'
        return 'default'

    def db_for_write(self, model, **hints):
        if model._meta.app_label in ['user_management', 'bug_management', 'project_management',
                                     'component_management', 'notification_management', 'attachment_management']:
            return model._meta.app_label + '_db'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in ['user_management', 'bug_management', 'project_management',
                         'component_management', 'notification_management', 'attachment_management']:
            # Allow migrations for all models of the specified app on its specific database
            return db == app_label + '_db'

        # For models outside the specified apps, allow migrations on the default database
        if db == 'default' and model_name is not None:
            model_app_label = model_name.split('.')[0]
            if model_app_label in ['user_management', 'bug_management', 'project_management',
                                   'component_management', 'notification_management', 'attachment_management']:
                return False

        return None
