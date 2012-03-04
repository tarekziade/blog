Title: To blob or not to blob ?
Date: 2007-09-14 16:08
Category: plone, zope

Back to the storing discussion: at this time we have a quite complete
tool to handle big files in Plone: File System Storage ([FSS][]).   

  
  
# [FSS Current features][]

  
The idea of this product is to provide a storage with a backup
mechanism, to be able to do some restore. It can handle big file and
store them on server-side with several strategies:   
-   Flat storage: All field values are stored in a flat structure. This
    strategy is the default one.
-   Directory storage strategy: All field values are stored in a
    directory structure.
-   Site storage strategy 1: All field values are stored in a directory
    structure mirroring structure of PloneSite. Backup files are stored
    in a flat structure.
-   Site storage strategy 2: All field values are stored in a directory
    structure mirroring structure of PloneSite. Backup files are stored
    in a flat structure.

  
More information on this here : [FSS Strategies][]   

  
  
# [A Blob Strategy ?][]

  
ZODB Blob, that are beeing integrated into Zope provide similar
features: it stores on the filesystem the file and provide access from
the ZODB. To configure such a storage, the zodb\_db section of zope.conf
would look like this:   

    <zodb_db main>

        # Main FileStorage database

        <blobstorage>



          blob-dir $INSTANCE/var/blobs

          <filestorage base="1">

            path $INSTANCE/var/Data.fs

          </filestorage>

        </blobstorage>

        mount-point /

    </zodb_db>

  
This tells Zope at startup to create a blob-compatible storage and
store blobs in the $INSTANCE/var/blobs folder. Then, the subsection
provide the regular Data.fs.   
  
Using this kind of configuration will let us use ZODB.blob APIs in the
code. To give a shot on blobs, I have created a new strategy on FSS,
that uses blobs. A base class handles blob readings and writings:   

    class ImplicitBlob(Implicit, blob.Blob):



        def __init__(self, title='', path='',

                     name='', mimetype='text/plain'):

            """stores blob metadata"""

            blob.Blob.__init__(self)

            self.title = title

            self.path = path

            self.mimetype = mimetype

            self.name = name



        def get_size(self):

            """Return the size of the blob."""



            file = self.open('r')

            try:

                file.seek(0, 2)

                result = file.tell()

            finally:

                file.close()

            return result



        def updateMetadata(self, **kwargs):

            """fills the metadata"""

            for key, value in kwargs.items():

                if key in self.__dict__:

                    setattr(self, key, value)



        def writeValue(self, value):

            """fills the blob"""

            file = self.open('w')

            try:

                file.write(value)

            finally:

                file.close()



        def getValue(self):

            """returns the blob whole content"""

            file = self.open('r')

            try:

                return file.read()

            finally:

                file.close()

  
The real version can be found in the collective repository in a
[branch][]. This Zope2-style code is not what I would have done in a new
product, but my goal was to quickly add the feature in FSS to make some
tries.   
  
It took me quite a time though, to set up the test fixture to be sure
to run the tests over a BlobStorage instead of a DemoStorage. You must
create a custom\_zodb.py file into your tests folder and make sure it's
called before the TestCase imports. Here's my file:   

    from ZODB.FileStorage.FileStorage import FileStorage

    from ZODB.MappingStorage import MappingStorage

    from ZODB.blob import BlobStorage

    from tempfile import mkdtemp



    base_storage = MappingStorage("test")

    blob_dir = mkdtemp()

    Storage = BlobStorage(blob_dir, base_storage)

  
(Thanks ZODB guys for using doctests in your code, that helped me much)
  
  
Once the ImplicitBlob is made available, I just addded a new strategy
in FSS that uses it this way:   
-   the tool becomes a BTreeFolder2 object and holds
    ImplicitBlobinstances in it;
-   each blob id is the file uid;
-   the strategy knows how to return a File object;

  
Now I can add FSSItem instances that are stored into blobs. And guess
what, it seems to work ;)   

  
  
# [What's next ?][]

  
Using blobs seems to be the future of FSS, because it has all the
features needed to store files. Furthermore blob are transactional, and
this is quite a difference with FSS's regular file storages, because in
that case, it's not necessary anymore to set up a NFS to be
ZEO-compatible. But all FSS strategies have use cases that we need to
keep. For example, the Site Storage Strategy is really sweet: user can
find back their file on the filesystem with the same name, etc. Even
though we know this is not really important technically speaking, it can
be reassuring for the customer.   
  
For large sites though, I wouldn't use blobs and would set up a
specialized co-server. Tramline fills the bill and we are thinking about
providing a tramline-friendly strategy in FSS, in order to provide
direct access to the files.   
  
But all of this is a work in process, and the blob strategy still needs
a lot of testing.

  [FSS]: http://ingeniweb.sourceforge.net/Products/FileSystemStorage
  [FSS Current features]: #id1 "fss-current-features"
  [FSS Strategies]: http://ingeniweb.sourceforge.net/Products/FileSystemStorage/#storage-strategies
  [A Blob Strategy ?]: #id2 "a-blob-strategy"
  [branch]: http://dev.plone.org/collective/browser/FileSystemStorage/branches/tarek_blob_support
  [What's next ?]: #id3 "what-s-next"
