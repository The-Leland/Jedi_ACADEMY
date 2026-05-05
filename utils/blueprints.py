


def register_blueprints(app):
 
    registrations = []

   
    from routes.auth_token_routes import auth
    app.register_blueprint(auth)
    registrations.append("routes.auth_token_routes.auth")

  
    from routes.user_routes import user
    app.register_blueprint(user)
    registrations.append("routes.user_routes.user")

  
    from routes.temple_routes import temple
    app.register_blueprint(temple)
    registrations.append("routes.temple_routes.temple")

    
    from routes.species_routes import species
    app.register_blueprint(species)
    registrations.append("routes.species_routes.species")

   
    from routes.master_routes import master
    app.register_blueprint(master)
    registrations.append("routes.master_routes.master")

    
    from routes.padawan_routes import padawan
    app.register_blueprint(padawan)
    registrations.append("routes.padawan_routes.padawan")

   
    from routes.crystal_routes import crystal
    app.register_blueprint(crystal)
    registrations.append("routes.crystal_routes.crystal")

   
    from routes.lightsaber_routes import lightsaber
    app.register_blueprint(lightsaber)
    registrations.append("routes.lightsaber_routes.lightsaber")

  
    from routes.course_routes import course
    app.register_blueprint(course)
    registrations.append("routes.course_routes.course")

   
    from routes.padawan_course_routes import padawan_course
    app.register_blueprint(padawan_course)
    registrations.append("routes.padawan_course_routes.padawan_course")

  
    if registrations:
        for r in registrations:
            print(f"Registered blueprint: {r}")

    else:
        print("No blueprints registered (check routes package).")
