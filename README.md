# A simple django application, with authentication and different lyers of authorisation.
- Its all a bout social media posts.
- Every post model has title, description and created_at properties.
- Users can create, read, update and delete posts following the rules below:
  - Anyone can show full list of the posts (titles, and creation time only) no login required.
  - Only logged in users can see post details (not to visit detail page).
  - Only logged in users can create posts.
  - Only a post author can update or delete it. 
- The data are stored using postgresql data base on heroku.
