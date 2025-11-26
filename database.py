    import sqlit3
    from datetime import datetime

    DB_FILE = 'students.db'

    def get_connection():
        """Get database connection"""
        conn = sqlit3.connect(DB_FILE)
        conn.row_factory = sqlit3.Row 
        return conn