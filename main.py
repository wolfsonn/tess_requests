import requests_db
import taxes

# create the database
# requests_db.create_db()

# add new request to database
# a prompt for requests images folder will appear
# requests_db.add_requests()

# get export for all requests
# requests_db.export_all_pending()

# or get export for a type of action - parameter: action
requests_db.export_one_pending('РБСС')

# set the status for a type of action to 'done' - parameter: action
requests_db.mark_done_one('РБСС')

# get due taxes for the export - parameter: action
taxes.get_taxes('РБСС')
