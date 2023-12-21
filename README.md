# Soundcheck DRF API

**Developer: Michael Roberts**

💻 [Live link](https://soundcheck-drf-api-15efb796f01f.herokuapp.com/)

This repository contains the API set up using Django REST Framework for the Soundcheck front-end application ([repository here]() and [live website here]())


## Table of Contents
  - [User Stories](#user-stories)
  - [Database](#database)
  - [Technologies Used](#technologies-used)
  - [Validation](#validation)
  - [Testing](#testing)
  - [Credits](#credits)


## User Stories
- As an admin user, I want to be able to create, edit and delete the users, posts, comments and likes, so that I can have a control over content posted on the application and remove any potentially inappropriate content.


## Database
The following models were created to represent the database model structure of the application:
<img src="docs/readme/soundcheck-database-diagram.png">

#### User Model
- The User model contains information about the user. It is part of the Django allauth library.
- One-to-one relation with the Profile model owner field
- ForeignKey relation with the Follower model owner and followed fields
- ForeignKey relation with the Post model owner field
- ForeignKey relation with the Comment model owner field
- ForeignKey relation with the Like model owner field

#### Profile Model
- The Profile model contains the following fields: owner, name,created_at, updated_at, content and image.
- One-to-one relation between the owner field and the User model id field.

#### Post Model
- The Post model contains the following fields: owner, created_at, updated_at, title, content and image.
- ForeignKey relation with the Comment model post field.
- ForeignKey relation with the Like model post field.

#### Comment Model
- The Comment model contains the following fields: owner, post, created_at, updated_at and content.
- ForeignKey relation between the owner field and the User model id field
- ForeignKey relation between the post field and the User model post field

#### Like Model
- The Like model contains the following fields: owner, post and created_at.
- ForeignKey relation between to the User model id field.
- ForeignKey relation between the owner field and the User model id field.
- ForeignKey relation between the post field and the Post model post field.

#### Follower Model
- The Follower model contains the following fields: owner, followed and created_at.
- ForeignKey relation between the owner field and the User model id field.
- ForeignKey relation between the followed field and the User model post field.


## Technologies Used
### Languages & Frameworks
- Python
- Django

### Libraries & Tools
- [Git](https://git-scm.com/) was used for version control via Gitpod terminal to push the code to GitHub
- [GitHub](https://github.com/) was used as a remote repository to store project code
- [Gitpod](https://gitpod.io/workspaces) - a virtual IDE workspace used to build this site
- [Django REST Framework](https://www.django-rest-framework.org/) was used to build the back-end API
- [Django AllAuth](https://django-allauth.readthedocs.io/en/latest/index.html) was used for user authentication
- [Cloudinary](https://cloudinary.com/) to store static files
- [Pillow](https://pillow.readthedocs.io/en/stable/) was used for image processing and validation
- [APITestCase](https://www.django-rest-framework.org/api-guide/testing/)Django Rest Framework APITestCase was used for automated testing
- [Heroku](https://heroku.com) was used to deploy the project into live environment
- [Psycopg2](https://www.psycopg.org/docs/) was used as a PostgreSQL database adapter for Python
- [ElephantSQL](https://www.postgresql.org/) – deployed project on Heroku uses an ElephantSQL database


## Validation
### PEP8 Validation
[Code Institute Python Linter (PEP8)](https://pep8ci.herokuapp.com/) validation service was used to check the code for PEP8 requirements. All the code passes with no errors or warnings.

<details><summary>Screenshots - PROFILES</summary>
    <details><summary>Models</summary>
    <img src="docs/validation/profiles_models_validation.png">
    </details>
    <details><summary>Serializers</summary>
    <img src="docs/validation/profiles_serializers_validation.png">
    </details>
    <details><summary>Tests</summary>
    <img src="docs/validation/profiles_tests_validation.png">
    </details>
    <details><summary>Urls</summary>
    <img src="docs/validation/profiles_urls_validation.png">
    </details>
    <details><summary>Views</summary>
    <img src="docs/validation/profiles_views_validation.png">
    </details>
</details>

<details><summary>Screenshots - POSTS</summary>
    <details><summary>Models</summary>
    <img src="docs/validation/posts_models_validation.png">
    </details>
    <details><summary>Serializers</summary>
    <img src="docs/validation/posts_serializers_validation.png">
    </details>
    <details><summary>Tests</summary>
    <img src="docs/validation/posts_tests_validation.png">
    </details>
    <details><summary>Urls</summary>
    <img src="docs/validation/posts_urls_validation.png">
    </details>
    <details><summary>Views</summary>
    <img src="docs/validation/posts_views_validation.png">
    </details>
</details>


## Testing
### Manual testing of user stories
- As an admin user, I want to be able to create, edit and delete the users, posts, comments and likes, so that I can have a control over content posted on the application and remove any potentially inappropriate content.

**Test** | **Action** | **Expected Result** | **Actual Result**
-------- | ------------------- | ------------------- | -----------------
User | Create, update & delete user | A user can be created, edited or deleted | Works as expected
User | Change permissions | User permissions can be updated | Works as expected
Profile | Create, update & delete | User profile can be created, edited or deleted | Works as expected
Post | Create, update & delete | A post can be created, edited or deleted | Works as expected
Comment | Create, update & delete | A comment can be created, edited or deleted | Works as expected
Like | Create & delete | A like can be created or deleted (like/unlike post) | Works as expected
Follower | Create & delete | Follow or unfollow user | Works as expected

In addition, posts, comments, likes and following can be created by logged-in users only. Users can only update or delete content posted by themselves.

<details><summary>Screenshots - USER</summary>
    <details><summary>Create user</summary>
    <img src="docs/testing/user_create_test_01.png">
    <img src="docs/testing/user_create_test_02.png">
    <img src="docs/testing/user_create_test_03.png">
    </details>
    <details><summary>Update user</summary>
    <img src="docs/testing/user_update_test_01.png">
    <img src="docs/testing/user_update_test_02.png">
    <img src="docs/testing/user_update_test_03.png">
    </details>
    <details><summary>Delete user</summary>
    <img src="docs/testing/user_delete_test_01.png">
    <img src="docs/testing/user_delete_test_02.png">
    <img src="docs/testing/user_delete_test_03.png">
    </details>
    <details><summary>Change user permissions</summary>
    <img src="docs/testing/user_change_permissions_test_01.png">
    <img src="docs/testing/user_change_permissions_test_02.png">
    <img src="docs/testing/user_change_permissions_test_03.png">
    </details>
</details>

<details><summary>Screenshots - PROFILE</summary>
    <details><summary>Update profile</summary>
    <img src="docs/testing/profile_update_test_01.png">
    <img src="docs/testing/profile_update_test_02.png">
    <img src="docs/testing/profile_update_test_03.png">
    </details>
    <details><summary>Delete profile</summary>
    <img src="docs/testing/profile_delete_test_01.png">
    <img src="docs/testing/profile_delete_test_02.png">
    <img src="docs/testing/profile_delete_test_03.png">
    </details>
    <details><summary>Create profile</summary>
    <img src="docs/testing/profile_create_test_01.png">
    <img src="docs/testing/profile_create_test_02.png">
    <img src="docs/testing/profile_create_test_03.png">
    </details>
</details>

<details><summary>Screenshots - POST</summary>
    <details><summary>Create post</summary>
    <img src="docs/testing/post_create_test_01.png">
    <img src="docs/testing/post_create_test_02.png">
    </details>
    <details><summary>Update post</summary>
    <img src="docs/testing/post_update_test_01.png">
    <img src="docs/testing/post_update_test_02.png">
    </details>
    <details><summary>Delete post</summary>
    <img src="docs/testing/post_delete_test_01.png">
    <img src="docs/testing/post_delete_test_02.png">
    <img src="docs/testing/post_delete_test_03.png">
    </details>
</details>

<details><summary>Screenshots - COMMENT</summary>
    <details><summary>Create comment</summary>
    <img src="docs/testing/comment_create_test_01.png">
    <img src="docs/testing/comment_create_test_02.png">
    </details>
    <details><summary>Update comment</summary>
    <img src="docs/testing/comment_update_test_01.png">
    <img src="docs/testing/comment_update_test_02.png">
    </details>
    <details><summary>Delete comment</summary>
    <img src="docs/testing/comment_delete_test_01.png">
    <img src="docs/testing/comment_delete_test_02.png">
    <img src="docs/testing/comment_delete_test_03.png">
    </details>
</details>

<details><summary>Screenshots - LIKE</summary>
    <details><summary>Create like</summary>
    <img src="docs/testing/like_create_test_01.png">
    <img src="docs/testing/like_create_test_02.png">
    <img src="docs/testing/like_create_test_02.png">
    </details>
    <details><summary>Delete like</summary>
    <img src="docs/testing/like_delete_test_01.png">
    <img src="docs/testing/like_delete_test_02.png">
    <img src="docs/testing/like_delete_test_03.png">
    </details>
</details>

<details><summary>Screenshots - FOLLOWER</summary>
    <details><summary>Create follow</summary>
    <img src="docs/testing/follower_create_test_01.png">
    <img src="docs/testing/follower_create_test_02.png">
    <img src="docs/testing/follower_create_test_02.png">
    </details>
    <details><summary>Delete follow</summary>
    <img src="docs/testing/follower_delete_test_01.png">
    <img src="docs/testing/follower_delete_test_02.png">
    <img src="docs/testing/follower_delete_test_03.png">
    </details>
</details>

### Automated testing
Automated testing was done using the Django Rest Framework APITestCase.

- Tests summary
<details><summary>Profiles Tests</summary>
<img src="docs/testing/apitest_soundcheck_profiles.png">
</details>

<details><summary>Posts Tests</summary>
<img src="docs/testing/apitest_soundcheck_posts.png">
</details>

<details><summary>Comments Tests</summary>
<img src="docs/testing/apitest_soundcheck_comments.png">
</details>

<details><summary>Likes Tests</summary>
<img src="docs/testing/apitest_soundcheck_likes.png">
</details>

<details><summary>Followers Tests</summary>
<img src="docs/testing/apitest_soundcheck_followers.png">
</details>

<details><summary>Combined Tests</summary>
<img src="docs/testing/apitest_soundcheck_combined.png">
</details>


## Credits
### Code
This project was created based on the Code Institute's Django REST API walkthrough project ['Moments'](https://github.com/Code-Institute-Solutions/drf-api).