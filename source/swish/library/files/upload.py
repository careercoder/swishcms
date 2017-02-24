# Required for S3 Uploads
import cStringIO
import mimetypes

# Import Amazon S3
from boto.s3.connection import S3Connection
from boto.s3.key import Key

from django.conf        import settings     # Application Configuration
import uuid

def uploadFile(request,  type='image',  from_field=False):

    try:
            file        = request.FILES[from_field]
            fileName    = request.FILES[from_field].name
    except:
        return False


    if type == 'resume':
        try:

            output = cStringIO.StringIO()
            output.write( file.read() )
            contents = output.getvalue()
            output.close()

            # STATRT Upload a File to Amazon S3
            # Get Keys
            aws_key       = settings.S3_ACCESS_KEY_ID
            aws_secret    = settings.S3_SECRET_ACCESS_KEY

            # connection
            conn = S3Connection(aws_key, aws_secret)

            mybucket = "startajobboard"
            bucketobj = conn.get_bucket(mybucket)

            tid = uuid.uuid4()

            resumeDirPath = str( 'resumes/' + str(tid) + '/' + str(fileName).lower())

            content = str(file.read())
            k = Key(bucketobj)
            k.key = resumeDirPath
            k.set_contents_from_string(contents)
            k.make_public()


            uploadedFile  = str(fileName).lower()


            filePath = 'https://startajobboard.s3.amazonaws.com/resumes/' + str(tid) + '/' + uploadedFile

            return filePath

        except:
            return False



    else:
        try:

            output = cStringIO.StringIO()
            output.write( file.read() )
            contents = output.getvalue()
            output.close()

            # STATRT Upload a File to Amazon S3
            # Get Keys
            aws_key       = settings.S3_ACCESS_KEY_ID
            aws_secret    = settings.S3_SECRET_ACCESS_KEY

            # connection
            conn = S3Connection(aws_key, aws_secret)

            mybucket = "startajobboard"
            bucketobj = conn.get_bucket(mybucket)

            resumeDirPath = str( 'jobboards/images/' + str(request.user.username) + '/') + str(request.user.id) + '-' + str(fileName).lower()

            # content = str(file.read())

            k = Key(bucketobj)
            k.key = resumeDirPath
            k.set_contents_from_string(contents)
            k.make_public()


            uploadedFile  = str(request.user.id) + '-' + str(fileName).lower()


            filePath = 'https://startajobboard.s3.amazonaws.com/jobboards/images/' + str(request.user.username) + '/' + uploadedFile

            return filePath

        except:
            return False





